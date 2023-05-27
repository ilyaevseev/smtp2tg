# smtp2tg

* Initial article published at March 2020: https://cdnnow.ru/blog/smtp2tg/
* Here is an improved version rewritten at May 2023. Tested under Ubuntu 20.04

### Quick install:

* apt install python3-requests dma bsd-mailx
* useradd -d /nonexistent -s /bin/false -r smtp2tg
* git clone https://github.com/ilyaevseev/smtp2tg.git
* cd smtp2tg
* sudo install -m640 -o root -g smtp2tg smtp2tg.ini /etc/default/smtp2tg.ini
* sudo install -m750 -o root -g smtp2tg smtp2tg.py /usr/local/bin/smtp2tg.py
* sudo install -m644 -o root -g root smtp2tg.service /etc/systemd/system/smtp2tg.service
* sudo install -m640 -o root -g mail dma.conf /etc/dma/dma.conf
* systemctl daemon-reload
* systemctl enable smtp2tg
* systemctl start smtp2tg
* systemctl status smtp2tg
* date | mail -s test1 who@is.me

Enjoy!
