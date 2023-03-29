#======================================= 本Web工具所用函数 =========================================#
# 库函数
from flask import Flask
from flask import request
from neo4j import GraphDatabase
from json import dumps
#**********************************************END*************************************************#


#======================================= Python-Flask基础配置 ======================================#
port = 8000                                                                 # 服务端口号
app = Flask(__name__, static_url_path="/static/")                           # 静态文件存储路径
#**********************************************END*************************************************#

@app.route("/")
def get_login():
    return app.send_static_file("index.html")

@app.route("/api/getattributesofnode", methods=['POST'], strict_slashes=False)
def api_getattributesofnode():    
    '''
        @ 功能：根据节点名获取节点属性
        @ 输入：节点名
        @ 输出：节点属性
    '''
    if request.method == 'POST':
        nodename = request.form['nodename']
        try:
            with System_Neo4j_Driver.session() as session:
                node_prop = list(session.run("MATCH (n) where n.name='"+nodename+"' return properties(n) AS properties"))[0]
            return dumps({'status':'success','resultdata':node_prop['properties']}) 
        except:
            return dumps({'status':'fail','resultdata':"获取失败，请检查存储介质的连接情况"})
            
#============================================= 主函数 =============================================#
if __name__ == "__main__":
    
    # 系统自检：利用已知数据库鉴权信息尝试连接Neo4j数据库
    uri = 'bolt://127.0.0.1:7687'
    username = 'neo4j'
    password = 'test'
    System_Neo4j_Driver = 'Neo4jDriver'
    System_Neo4j_Driver = GraphDatabase.driver(uri, auth=(username,password))
    print(type(System_Neo4j_Driver))
    
    # 启动服务
    app.run(host='127.0.0.1',port=port)
#**********************************************END*************************************************#