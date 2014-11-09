import java.io.*;
import java.util.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class MyCommon {
	public static final String STUDENT_ID_SET_PATH = "D:/Workspace/AdResearch/WebRoot/query_set/cookie_user_query_map.txt";
	public static final String QUERY_PATH = "D:/Workspace/AdResearch/WebRoot/query_set/query_description.txt";
	public static final String DESCRIPTION_PAGE = "D:/Workspace/AdResearch/WebRoot/pages/QueryDescription.html";
	public static Vector<String> desStrings = null;
	public static HashMap<String, Vector<Integer>> userQueryMap = null;
	public static HashMap<Integer, String> queryIDMap = null;
	public static HashMap<Integer, String> queryDescriptionMap = null;
	public static void initUserQueryMap(){
		if(MyCommon.userQueryMap == null){
        	MyCommon.userQueryMap = MyCommon.loadUserQueryMap(MyCommon.STUDENT_ID_SET_PATH);
        }
		if(MyCommon.queryIDMap == null){
			Vector<HashMap<Integer, String>> ret = MyCommon.loadQueryInfo(MyCommon.QUERY_PATH);
			MyCommon.queryIDMap = ret.get(0);
			MyCommon.queryDescriptionMap = ret.get(1); 
		}
		if(MyCommon.desStrings == null){
			MyCommon.desStrings = MyCommon.loadDesInfo(DESCRIPTION_PAGE);
		}
	}
	public static Vector<String> loadDesInfo(String path){
		Vector<String> ret = new Vector<String>();
		try {
			BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(path)));
			String line;
			while((line = reader.readLine()) != null){
				ret.add(line);
			}
			reader.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return ret;
	}
	
	public static Vector<HashMap<Integer, String>> loadQueryInfo(String path){
		Vector<HashMap<Integer, String>> ret = new Vector<HashMap<Integer, String>>();
		HashMap<Integer, String> qId = new HashMap<Integer, String>();
		HashMap<Integer, String> qDes = new HashMap<Integer, String>();
		ret.add(qId);
		ret.add(qDes);
		try {
			BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(path), "utf-8"));
			String line;
			reader.readLine();
			while((line = reader.readLine()) != null){
				String[] list = line.trim().split("\t");
				if(list.length >= 3){
					int id = Integer.parseInt(list[0]);
					qId.put(id, list[1]);
					qDes.put(id, list[2]);
					System.out.println("Query " + line.trim());
				}
			}
			reader.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return ret;
	}
	
	public static HashMap<String, Vector<Integer>> loadUserQueryMap(String path){
		HashMap<String, Vector<Integer>> map = new HashMap<String, Vector<Integer>>();
		try {
				BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(path), "utf-8"));
				String line;
				while((line = reader.readLine()) != null){
					String[] list = line.trim().split("\t");
				if(list.length >= 1){
					map.put(list[0], new Vector<Integer>());
				}
				for(int i = 1; i < list.length; i ++){
					try{
						int index = Integer.parseInt(list[i]);
						map.get(list[0]).add(index);
					}catch(Exception ecp){
						System.out.println("ERR: " + list[i]);
					}
				}
				System.out.println("Add " + line.trim());
			}
			reader.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return map;
	}
	
	public static Cookie MyCookie(String name, String value){
		Cookie cookie = new Cookie(name,value); 
		cookie.setMaxAge(3*24*60*60);   
		cookie.setPath("/");   
		return cookie;
	}
	
	public static void addUniqueCookie(HttpServletRequest request, HttpServletResponse response, String name, String value){
		Cookie mycookies[] = request.getCookies();
		Cookie cookie = MyCookie(name, value);
		if(mycookies != null){
			for(Cookie c: mycookies){
				if(c.getName().equals(name)){
					cookie = c;
					cookie.setValue(value);
					cookie.setPath("/");
					cookie.setMaxAge(3*24*60*60);
				}
			}
		}
		response.addCookie(cookie);
	}
	public static String getCookie(HttpServletRequest request, String name){
		String ret = "";
		Cookie mycookies[] = request.getCookies();
		if(mycookies != null){
			for(Cookie c: mycookies){
				if(c.getName().equals(name)){
					ret = c.getValue();
					break;
				}
			}
		}
		return ret;
	}
}	
