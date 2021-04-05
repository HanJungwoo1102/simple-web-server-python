# simple-web-server-python

프레임워크, 라이브러리를 사용하지 않고 소켓 프로그래밍을 통해 http request 를 처리할 수 있는 web server 를 만들어 보았다.

```
python3 start-test-web-server.py
```

브라우저에서 [웹서버](http://localhost:3000) 에 접근해서 serving 할 html 파일이 있으면 status 200 에 html 파일을 response 하고 없으면 status 404 를 response 한다.

http://localhost:3000/requestedFile.html

-> response: status 200, requestedFile.html 

http://localhost:3000/

-> response: status 404
