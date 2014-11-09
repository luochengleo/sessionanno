2014.2.25
1.更改任务顺序，将navigational和informational的任务交叉，改动详见\AdResearch\WebRoot\query_set\user_query_map.xlsx
2.修改\AdResearch\WebRoot\pages\des_X.html的任务序号显示，使实际显示与任务次序相符

2014.1.3
1.在wc_log.js中添加任务结束提示语，添加点击“浏览完成”按钮时（check_state=1）返回客户端当地时间戳的功能

2013.12.28
1.更新“个人贷款服务”的任务描述，使之更加贴近实际情况
2.添加page1和page2中中国移动条目的摘要显示

2013.12.26
1.修改用户列表
2.在LoginService.java中添加对空ID的识别和跳转

2013.12.25
1.更新背色页面的展示样式，使双行摘要显示更加自然，在style_2_2.css中添加WCAd样式描述
2.更新conf中的style_1.css style_2_1.css和style_2_2.css中WCResult的样式：去除style_1.css中关于WCResult样式，在style_2_1.css中添加WCResult的样式中添加float：left属性
3.修正了背色页面中‘推广链接’链接错误的问题
4.修改wclog.js中关于jump_out的记录规则，由于有输入框，blur事件会同时触发输入框以及window的blur事件是jump_out出现两次，加入判断flag使之记录正确
5.修正“五粮液专卖”结果页面中的显示错误

2013.12.22
1.配置显示页面
2.修改wc_log.js中relevance_search的log记录