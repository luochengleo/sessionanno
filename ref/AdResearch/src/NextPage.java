

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.*;

/**
 * Servlet implementation class NextPage
 */
@WebServlet("/NextPage")
public class NextPage extends HttpServlet {
	private static final long serialVersionUID = 1L;
    /**
     * @see HttpServlet#HttpServlet()
     */
    public NextPage() {
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
		if(!MyCommon.userQueryMap.containsKey(studentID)){
			//response.sendRedirect("/Research4Plus/Login.html"); 
			response.sendRedirect("Login.html"); 
		}else{ 
			String currentQueryID = request.getParameter("currentQueryID");
			int cid = Integer.parseInt(currentQueryID);
			int nid = -2;
			int sid = -2;
			Vector<Integer> queryList = MyCommon.userQueryMap.get(studentID);
			for(int i = 0; i <queryList.size(); i ++){
				if(cid == -1 || (i > 0 && cid == queryList.get(i - 1))){
					nid = queryList.get(i);
					sid = i;
					break;
				}
			}
			MyCommon.addUniqueCookie(request, response, "currentQueryID", "" + nid);
			//response.addCookie(MyCommon.MyCookie("currentQueryID", "" + nid));
			if(nid == -2){
				MyCommon.addUniqueCookie(request, response, "currentQueryID", "-1");
				//response.sendRedirect("/Research4Plus/End.html");
				response.sendRedirect("End.html");
			}else if(nid == -1){
				//response.sendRedirect("/Research4Plus/Describe.html");
				response.sendRedirect("Describe.html");
			}else{
//				PrintWriter pw = response.getWriter();
//				for(String s: MyCommon.desStrings){
//					//System.out.println("+++++nid=" + nid);
//					s = s.replace("query_position", MyCommon.queryIDMap.get(nid));
//					s = s.replace("description_position", MyCommon.queryDescriptionMap.get(nid));
//					s = s.replace("url_position", "/research4_query_page/plus_"+ nid + ".html");
//					pw.println(s);
//				} 
//				pw.flush();
//				pw.close();
				response.sendRedirect("./pages/des_"+ nid + ".html?id=" + sid);
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
