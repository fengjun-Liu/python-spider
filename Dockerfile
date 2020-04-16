FROM python:latest
MAINTAINER Liufengjun <939643949@qq.com>

RUN pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /usr/src/myqpp
VOLUME /usr/src/myapp

CMD ["python"]
