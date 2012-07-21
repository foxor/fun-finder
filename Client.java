import com.fun_finder.FunFinderProtos.GameInitMessage;
import com.fun_finder.FunFinderProtos.FunMessage;
import com.fun_finder.FunFinderProtos.FunProperty;

import java.net.*;
import java.io.*;
import java.util.*;

public class Client
{

  private class PropertyWrapper
  {
    public List<Integer> values;
    public List<Boolean> changed;

    public PropertyWrapper(GameInitMessage gim)
    {
      values = new ArrayList<Integer>();
      changed = new ArrayList<Boolean>();
      for (FunProperty fp : gim.getInitialConfig().getBaselineList())
      {
        values.add(fp.getValue());
        changed.add(false);
      }
    }
  }

  private PropertyWrapper properties;
  private String gameId;

  public Client()
  {
  }

  public static void main(String[] argv) throws Exception
  {
    Client client = new Client();
    client.start();
    client.end();
  }

  public void start() throws Exception
  {
    URL url = new URL("http://localhost:5000/gameInit");
    URLConnection urlCon = url.openConnection();
    GameInitMessage gim = GameInitMessage.parseFrom(urlCon.getInputStream());
    urlCon.getInputStream().close();
    this.properties = new PropertyWrapper(gim);
    gameId = gim.getGameId();
  }

  public int rate()
  {
    int score = 0;
    int cur = 1;
    for (int i = 0; i < properties.values.size(); i++)
    {
      score += 10000 - Math.min(10000, Math.abs((1 << i) - properties.values.get(i)));
    }
    return score;
  }

  public void end() throws Exception
  {
    FunMessage.Builder fm = FunMessage.newBuilder()
      .setGameId(gameId)
      .setFunScore(rate());
    URL url = new URL("http://localhost:5000/gameFinish");
    URLConnection urlCon = url.openConnection();
    urlCon.setDoOutput(true);
    OutputStreamWriter wr = new OutputStreamWriter(urlCon.getOutputStream());
    wr.write("rating=");
    wr.flush();
    fm.build().writeTo(urlCon.getOutputStream());
    urlCon.getOutputStream().close();

    // No network I/O happens until you ask for feedback apparently
    urlCon.getInputStream();
  }
}
