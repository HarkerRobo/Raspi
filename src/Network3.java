import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

/**
 * 
 */

/**
 * @author joelmanning
 *
 */
public class Network3 extends Thread {
	
	public static final int PORT = 6000;
	
	private ServerSocket sock;
	private List<Handler> handlers;
	
	public static void main(String[] args){
		(new Network3()).run();
	}
	
	public Network3(){
		try {
			handlers = new ArrayList<Handler>();
			sock = new ServerSocket(PORT);
		} catch(IOException e) {
			e.printStackTrace();
			System.exit(1);
		}
	}
	
	public void run(){
		while(true){
			try {
				Handler h = new Handler(sock.accept());
				handlers.add(h);
				h.start();
			} catch(IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	public void messageRecieved(Object obj){
		System.out.println(obj);
	}
	
	public void broadcast(Object obj){
		for(Handler h: handlers){
			h.send(obj);
		}
	}
	
	class Handler extends Thread {
		
		private Socket s;
		private ObjectInputStream ois;
		private ObjectOutputStream oos;
		
		public Handler(Socket s){
			this.s = s;
			try {
				ois = new ObjectInputStream(s.getInputStream());
				oos = new ObjectOutputStream(s.getOutputStream());
			} catch(IOException e) {
				e.printStackTrace();
			}
		}
		
		public void send(Object o){
			try {
				oos.writeObject(o);
				oos.flush();
			} catch(IOException e) {
				e.printStackTrace();
			}
		}
		
		@Override
		public void run(){
			while(true){
				try {
					Object obj = ois.readObject();
					messageRecieved(obj);
				} catch(ClassNotFoundException e) {
					e.printStackTrace();
				} catch(IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
}
