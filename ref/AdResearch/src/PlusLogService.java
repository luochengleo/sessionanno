

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * Servlet implementation class PlusLogService
 */
@WebServlet("/PlusLogService")
public class PlusLogService extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private static Logger log = LogManager.getLogger("Plus");
	//private static Logger log = LogManager.getLogger("trace");
	
	public void wirteInfo(String info){
		log.info(info);
	}
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public PlusLogService() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		try {
			request.setCharacterEncoding("UTF-8");
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		response.setContentType("text/html;charset=UTF-8");
		/*String messageType = request.getParameter("mt");
		String user = request.getParameter("user");
		if(user == null || user.equals("")){
			user = "UnknownUser";
		}
		
		if(messageType.equals("Mouse")){
			String message = request.getParameter("message");
			message = URLDecoder.decode(message,"UTF-8");
			wirteInfo(user + "\t" + message);
		}else if(messageType.equals("Score")){
			
		}else if(messageType.equals("Check")){
			
		}*/
		String remoteAddr = request.getRemoteAddr();
		String message = request.getParameter("message");
		if(message != null){
			message = URLDecoder.decode(message,"UTF-8");
			String[] ms = message.split("\n");
			for(String m:ms){
				wirteInfo("IP:" + remoteAddr + "\t" + m);
			}
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		this.doGet(request, response);
	}

}
