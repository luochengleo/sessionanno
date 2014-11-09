

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.*;
import java.io.*;

/**
 * Servlet implementation class LoginService
 */
@WebServlet("/LoginService")
public class LoginService extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginService() {
        super();
        // TODO Auto-generated constructor stub
        MyCommon.initUserQueryMap();
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/html;charset=utf-8");
		String studentID = request.getParameter("studentID");
		if(!MyCommon.userQueryMap.containsKey(studentID)||studentID.equals("")){
			//response.sendRedirect("/Research4Plus/Login.html"); 
			response.sendRedirect("Login.html"); 
		}else{ 
			if(!MyCommon.getCookie(request, "studentID").equals(studentID)){
				MyCommon.addUniqueCookie(request, response, "studentID", studentID);
				MyCommon.addUniqueCookie(request, response, "currentQueryID", "-1");
			}
			//response.sendRedirect("/Research4Plus/Describe.html");
			response.sendRedirect("Describe.html");
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
