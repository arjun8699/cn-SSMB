import streamlit as st

# Function to display code examples
def display_code(code: str):
    st.code(code, language='python')

# Code examples
echo_client = '''
# server Code
import java.io.*;
import java.net.*;

class server {
    public static void main(String args[]) {
        String buff;
        ServerSocket s;
        Socket in;

        try {
            s = new ServerSocket(4550);
            in = s.accept();

            BufferedReader b = new BufferedReader(new InputStreamReader(in.getInputStream()));
            PrintWriter pw = new PrintWriter(in.getOutputStream(), true);

            System.out.println("Connection Established");

            buff = b.readLine();
            System.out.println("client said " + buff);
            pw.println(buff);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
'''
'''
# client code
import java.io.*;
import java.net.*;

class client {
    public static void main(String args[]) {
        String buff;
        Socket s;

        try {
            s = new Socket("127.0.0.1", 4550);

            BufferedReader b = new BufferedReader(new InputStreamReader(System.in));
            BufferedReader bl = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter pw = new PrintWriter(s.getOutputStream(), true);

            System.out.println("Connection Established");
            System.out.println("Enter the data...........");

            buff = b.readLine();
            pw.println(buff);

            buff = bl.readLine();
            System.out.println(buff);
            System.out.println("Echo Received");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

'''

exp_6B = '''
# server code

import java.net.*;
import java.io.*;

public class TCPServer {

    public static void main(String s[]) throws IOException {
        // Initialising the ServerSocket
        ServerSocket sok = new ServerSocket(3128);

        // Gives the Server Details Machine name, Port number
        System.out.println("Server Started " + sok);

        // Makes a socket connection to particular client after
        // which two way communication takes place
        Socket so = sok.accept();

        System.out.println("Client Connected " + so);

        InputStream in = so.getInputStream();
        OutputStream os = so.getOutputStream();

        PrintWriter pr = new PrintWriter(os, true);
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        BufferedReader brl = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String clientMsg = br.readLine();
            if (clientMsg == null) break;
            System.out.println("Msg frm client: " + clientMsg);

            System.out.print("Msg to client: ");
            String serverReply = brl.readLine();
            pr.println(serverReply);
        }

        // Cleanup
        br.close();
        brl.close();
        pr.close();
        so.close();
        sok.close();
    }
}
'''
'''
# client code
import java.net.*;
import java.io.*;

public class TCPClient {

    public static void main(String s[]) throws IOException {
        Socket sok = new Socket("localhost", 3128);

        InputStream in = sok.getInputStream();
        OutputStream ou = sok.getOutputStream();

        PrintWriter pr = new PrintWriter(ou, true); // auto-flush enabled
        BufferedReader brl = new BufferedReader(new InputStreamReader(in));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            System.out.print("Msg to Server: ");
            String msgToServer = br.readLine();
            pr.println(msgToServer);

            String msgFromServer = brl.readLine();
            if (msgFromServer == null) break;
            System.out.println("Msg frm server: " + msgFromServer);
        }

        // Cleanup
        br.close();
        brl.close();
        pr.close();
        sok.close();
    }
}

'''

exp_UDP = '''
#client code
import java.io.*;
import java.net.*;

class UDPClient {
    public static void main(String args[]) throws Exception {
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        DatagramSocket clientSocket = new DatagramSocket();
        InetAddress IPAddress = InetAddress.getByName("localhost");

        byte[] sendData = new byte[1024];
        byte[] receiveData = new byte[1024];

        System.out.print("Enter message: ");
        String sentence = inFromUser.readLine();
        sendData = sentence.getBytes();

        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);
        clientSocket.send(sendPacket);

        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        clientSocket.receive(receivePacket);

        String modifiedSentence = new String(receivePacket.getData(), 0, receivePacket.getLength());
        System.out.println("FROM SERVER: " + modifiedSentence);

        clientSocket.close();
    }
}
'''
'''
# server code
import java.io.*;
import java.net.*;

class UDPServer {
    public static void main(String args[]) throws Exception {
        DatagramSocket serverSocket = new DatagramSocket(9876);
        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];

        while (true) {
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
            serverSocket.receive(receivePacket);

            String sentence = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("RECEIVED: " + sentence);

            InetAddress IPAddress = receivePacket.getAddress();
            int port = receivePacket.getPort();

            String capitalizedSentence = sentence.toUpperCase();
            sendData = capitalizedSentence.getBytes();

            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);
            serverSocket.send(sendPacket);
        }
    }
}

'''

# Streamlit App Layout
st.title("CN Practical")

# Sidebar for selecting experiments
selected_experiment = st.sidebar.selectbox(
    "Select an Experiment", 
    ["echo_client", "exp_6B", "exp_UDP", ]
)

# Display corresponding code
if selected_experiment == "echo_client":
    st.header("echo_client")
    display_code(echo_client)
elif selected_experiment == "exp_6B":
    st.header("exp_6B")
    display_code(exp_6B)
elif selected_experiment == "exp_UDP":
    st.header("exp_UDP")
    display_code(exp_UDP)
