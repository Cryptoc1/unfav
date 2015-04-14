�
�*Uc           @   sF   d  d l  m Z m Z d e f d �  �  YZ d e f d �  �  YZ d S(   i����(   t   jsont   TwitterErrort
   UserStatusc           B   sn   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z e d
 �  � Z RS(   s'  A class representing the UserStatus structure used by the twitter API.
  
    The UserStatus structure exposes the following properties:
  
      userstatus.name
      userstatus.id_str
      userstatus.id
      userstatus.screen_name
      userstatus.following
      userstatus.followed_by
    c         K   sm   i d d 6d d 6d d 6d d 6d d 6d d 6} x6 | j �  D]( \ } } t |  | | j | | � � q= Wd S(   sj  An object to hold a Twitter user status message.
    
        This class is normally instantiated by the twitter.Api class and
        returned in a sequence.
    
        Args:
          id:
            The unique id of this status message. [Optional]
          id_str:
            The string version of the unique id of this status message. [Optional]
        t   namet   idt   id_strt   screen_namet	   followingt   followed_byN(   t   Nonet	   iteritemst   setattrt   get(   t   selft   kwargst   param_defaultst   paramt   default(    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   __init__   s    
c         C   s   |  j  p t S(   N(   R   t   False(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetFollowedBy*   s    c         C   s   |  j  p t S(   N(   R   R   (   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetFollowing-   s    c         C   s   |  j  S(   N(   R   (   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetScreenName0   s    c         C   s   |  j  | � S(   N(   t   __eq__(   R   t   other(    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   __ne__3   s    c         C   s�   yt | or |  j  | j  k or |  j | j k or |  j | j k or |  j | j k or |  j | j k or |  j | j k SWn t k
 r� t SXd  S(   N(   R   R   R   R   R   R   t   AttributeErrorR   (   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   6   s    c         C   s
   |  j  �  S(   s�   A string representation of this twitter.UserStatus instance.
    
        The return value is the same as the JSON string representation.
    
        Returns:
          A string representation of this twitter.UserStatus instance.
        (   t   AsJsonString(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   __str__B   s    c         C   s   t  j |  j �  d t �S(   s�   A JSON string representation of this twitter.UserStatus instance.
    
        Returns:
          A JSON string representation of this twitter.UserStatus instance
       t	   sort_keys(   R    t   dumpst   AsDictt   True(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   L   s    c         C   s�   i  } |  j  r |  j  | d <n  |  j r8 |  j | d <n  |  j rQ |  j | d <n  |  j rj |  j | d <n  |  j r� |  j | d <n  |  j r� |  j | d <n  | S(   s�   A dict representation of this twitter.UserStatus instance.
    
        The return value uses the same key names as the JSON representation.
    
        Return:
          A dict representing this twitter.UserStatus instance
        R   R   R   R   R   R   (   R   R   R   R   R   R   (   R   t   data(    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   T   s    						c         C   s�   d } d } d |  k rM d |  d k r1 t } n  d |  d k rM t } qM n  t d |  j d d � d |  j d d � d |  j d d � d |  j d d � d | d | � S(	   s�   Create a new instance based on a JSON dict.
    
        Args:
          data: A JSON dict, as converted from the JSON in the twitter API
        Returns:
          A twitter.UserStatus instance
        t   connectionsR   R   R   R   R   R   N(   R	   R    R   R   (   R!   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   NewFromJsonDictk   s    		(   t   __name__t
   __module__t   __doc__R   R   R   R   R   R   R   R   R   t   staticmethodR#   (    (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR      s   							
		t   Userc           B   s�  e  Z d  Z d �  Z d �  Z d �  Z e e e d d �Z d �  Z d �  Z	 e e e	 d d �Z
 d	 �  Z d
 �  Z e e e d d �Z d �  Z d �  Z e e e d d �Z d �  Z d �  Z e e e d d �Z d �  Z d �  Z e e e d d �Z d �  Z d �  Z e e e d d �Z d �  Z d �  Z e e e d d �Z d �  Z d �  Z e e e d d �Z d �  Z  d �  Z! e e  e! d d  �Z" d! �  Z# d" �  Z$ e e# e$ � Z% d# �  Z& d$ �  Z' e e& e' � Z( d% �  Z) d& �  Z* e e) e* � Z+ d' �  Z, d( �  Z- e e, e- � Z. d) �  Z/ d* �  Z0 e e/ e0 � Z1 d+ �  Z2 d, �  Z3 e e2 e3 � Z4 d- �  Z5 d. �  Z6 e e5 e6 � Z7 d/ �  Z8 d0 �  Z9 e e8 e9 d d1 �Z: d2 �  Z; d3 �  Z< e e; e< d d4 �Z= d5 �  Z> d6 �  Z? e e> e? d d7 �Z@ d8 �  ZA d9 �  ZB e eA eB d d: �ZC d; �  ZD d< �  ZE e eD eE d d= �ZF d> �  ZG d? �  ZH e eG eH d d@ �ZI dA �  ZJ dB �  ZK e eJ eK d dC �ZL dD �  ZM dE �  ZN e eM eN d dF �ZO dG �  ZP dH �  ZQ e eP eQ d dI �ZR dJ �  ZS dK �  ZT e eS eT d dL �ZU dM �  ZV dN �  ZW e eV eW d dO �ZX dP �  ZY dQ �  ZZ e eY eZ d dR �Z[ dS �  Z\ dT �  Z] dU �  Z^ dV �  Z_ dW �  Z` ea dX �  � Zb RS(Y   s�  A class representing the User structure used by the twitter API.
  
    The User structure exposes the following properties:
  
      user.id
      user.name
      user.screen_name
      user.location
      user.description
      user.default_profile
      user.default_profile_image
      user.profile_image_url
      user.profile_background_tile
      user.profile_background_image_url
      user.profile_banner_url
      user.profile_sidebar_fill_color
      user.profile_background_color
      user.profile_link_color
      user.profile_text_color
      user.protected
      user.utc_offset
      user.time_zone
      user.url
      user.status
      user.statuses_count
      user.followers_count
      user.friends_count
      user.favourites_count
      user.geo_enabled
      user.verified
      user.lang
      user.notifications
      user.contributors_enabled
      user.created_at
      user.listed_count
    c         K   s  i d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d	 6d  d
 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6d  d 6} x6 | j �  D]( \ } } t |  | | j | | � � q� Wd  S(    NR   R   R   t   locationt   descriptiont   default_profilet   default_profile_imaget   profile_image_urlt   profile_background_tilet   profile_background_image_urlt   profile_banner_urlt   profile_sidebar_fill_colort   profile_background_colort   profile_link_colort   profile_text_colort	   protectedt
   utc_offsett	   time_zonet   followers_countt   friends_countt   statuses_countt   favourites_countt   urlt   statust   geo_enabledt   verifiedt   langt   notificationst   contributors_enabledt
   created_att   listed_count(   R	   R
   R   R   (   R   R   R   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   �   sD    
c         C   s   |  j  S(   sc   Get the unique id of this user.
    
        Returns:
          The unique id of this user
        (   t   _id(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetId�   s    c         C   s   | |  _  d S(   se   Set the unique id of this user.
    
        Args:
          id: The unique id of this user.
        N(   RE   (   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetId�   s    t   docs   The unique id of this user.c         C   s   |  j  S(   sc   Get the real name of this user.
    
        Returns:
          The real name of this user
        (   t   _name(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetName�   s    c         C   s   | |  _  d S(   sf   Set the real name of this user.
    
        Args:
          name: The real name of this user
        N(   RI   (   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetName�   s    s   The real name of this user.c         C   s   |  j  S(   su   Get the short twitter name of this user.
    
        Returns:
          The short twitter name of this user
        (   t   _screen_name(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   �   s    c         C   s   | |  _  d S(   s   Set the short twitter name of this user.
    
        Args:
          screen_name: the short twitter name of this user
        N(   RL   (   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetScreenName�   s    s$   The short twitter name of this user.c         C   s   |  j  S(   sw   Get the geographic location of this user.
    
        Returns:
          The geographic location of this user
        (   t	   _location(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetLocation	  s    c         C   s   | |  _  d S(   s~   Set the geographic location of this user.
    
        Args:
          location: The geographic location of this user
        N(   RN   (   R   R)   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetLocation  s    s%   The geographic location of this user.c         C   s   |  j  S(   s}   Get the short text description of this user.
    
        Returns:
          The short text description of this user
        (   t   _description(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetDescription  s    c         C   s   | |  _  d S(   s�   Set the short text description of this user.
    
        Args:
          description: The short text description of this user
        N(   RQ   (   R   R*   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetDescription$  s    s(   The short text description of this user.c         C   s   |  j  S(   si   Get the homepage url of this user.
    
        Returns:
          The homepage url of this user
        (   t   _url(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetUrl/  s    c         C   s   | |  _  d S(   sk   Set the homepage url of this user.
    
        Args:
          url: The homepage url of this user
        N(   RT   (   R   R<   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetUrl7  s    s   The homepage url of this user.c         C   s   |  j  S(   sy   Get the url of the thumbnail of this user.
    
        Returns:
          The url of the thumbnail of this user
        (   t   _profile_image_url(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileImageUrlB  s    c         C   s   | |  _  d S(   s�   Set the url of the thumbnail of this user.
    
        Args:
          profile_image_url: The url of the thumbnail of this user
        N(   RW   (   R   R-   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileImageUrlJ  s    s&   The url of the thumbnail of this user.c         C   s   |  j  S(   s�   Boolean for whether to tile the profile background image.
    
        Returns:
          True if the background is to be tiled, False if not, None if unset.
        (   t   _profile_background_tile(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileBackgroundTileU  s    c         C   s   | |  _  d S(   s�   Set the boolean flag for whether to tile the profile background image.
    
        Args:
          profile_background_tile: Boolean flag for whether to tile or not.
        N(   RZ   (   R   R.   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileBackgroundTile]  s    s1   Boolean for whether to tile the background image.c         C   s   |  j  S(   N(   t   _profile_background_image_url(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileBackgroundImageUrlh  s    c         C   s   | |  _  d  S(   N(   R]   (   R   R/   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileBackgroundImageUrlk  s    s/   The url of the profile background of this user.c         C   s   |  j  S(   N(   t   _profile_banner_url(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileBannerUrlq  s    c         C   s   | |  _  d  S(   N(   R`   (   R   R0   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileBannerUrlt  s    s+   The url of the profile banner of this user.c         C   s   |  j  S(   N(   t   _profile_sidebar_fill_color(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileSidebarFillColorz  s    c         C   s   | |  _  d  S(   N(   Rc   (   R   R1   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileSidebarFillColor}  s    c         C   s   |  j  S(   N(   t   _profile_background_color(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileBackgroundColor�  s    c         C   s   | |  _  d  S(   N(   Rf   (   R   R2   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileBackgroundColor�  s    c         C   s   |  j  S(   N(   t   _profile_link_color(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileLinkColor�  s    c         C   s   | |  _  d  S(   N(   Ri   (   R   R3   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileLinkColor�  s    c         C   s   |  j  S(   N(   t   _profile_text_color(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProfileTextColor�  s    c         C   s   | |  _  d  S(   N(   Rl   (   R   R4   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProfileTextColor�  s    c         C   s   |  j  S(   N(   t
   _protected(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetProtected�  s    c         C   s   | |  _  d  S(   N(   Ro   (   R   R5   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetProtected�  s    c         C   s   |  j  S(   N(   t   _utc_offset(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetUtcOffset�  s    c         C   s   | |  _  d  S(   N(   Rr   (   R   R6   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetUtcOffset�  s    c         C   s   |  j  S(   s�   Returns the current time zone string for the user.
    
        Returns:
          The descriptive time zone string for the user.
        (   t
   _time_zone(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetTimeZone�  s    c         C   s   | |  _  d S(   s�   Sets the user's time zone string.
    
        Args:
          time_zone:
            The descriptive time zone to assign for the user.
        N(   Ru   (   R   R7   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetTimeZone�  s    c         C   s   |  j  S(   s{   Get the latest twitter.Status of this user.
    
        Returns:
          The latest twitter.Status of this user
        (   t   _status(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt	   GetStatus�  s    c         C   s   | |  _  d S(   s�   Set the latest twitter.Status of this user.
    
        Args:
          status:
            The latest twitter.Status of this user
        N(   Rx   (   R   R=   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt	   SetStatus�  s    s'   The latest twitter.Status of this user.c         C   s   |  j  S(   sz   Get the friend count for this user.
    
        Returns:
          The number of users this user has befriended.
        (   t   _friends_count(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetFriendsCount�  s    c         C   s   | |  _  d S(   s�   Set the friend count for this user.
    
        Args:
          count:
            The number of users this user has befriended.
        N(   R{   (   R   t   count(    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetFriendsCount�  s    s$   The number of friends for this user.c         C   s   |  j  S(   sv   Get the listed count for this user.
    
        Returns:
          The number of lists this user belongs to.
        (   t   _listed_count(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetListedCount�  s    c         C   s   | |  _  d S(   s�   Set the listed count for this user.
    
        Args:
          count:
            The number of lists this user belongs to.
        N(   R   (   R   R}   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetListedCount�  s    s)   The number of lists this user belongs to.c         C   s   |  j  S(   sw   Get the follower count for this user.
    
        Returns:
          The number of users following this user.
        (   t   _followers_count(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetFollowersCount�  s    c         C   s   | |  _  d S(   s�   Set the follower count for this user.
    
        Args:
          count:
            The number of users following this user.
        N(   R�   (   R   R}   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetFollowersCount  s    s(   The number of users following this user.c         C   s   |  j  S(   s�   Get the number of status updates for this user.
    
        Returns:
          The number of status updates for this user.
        (   t   _statuses_count(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetStatusesCount  s    c         C   s   | |  _  d S(   s�   Set the status update count for this user.
    
        Args:
          count:
            The number of updates for this user.
        N(   R�   (   R   R}   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetStatusesCount  s    s$   The number of updates for this user.c         C   s   |  j  S(   s|   Get the number of favourites for this user.
    
        Returns:
          The number of favourites for this user.
        (   t   _favourites_count(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetFavouritesCount!  s    c         C   s   | |  _  d S(   s�   Set the favourite count for this user.
    
        Args:
          count:
            The number of favourites for this user.
        N(   R�   (   R   R}   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetFavouritesCount)  s    s'   The number of favourites for this user.c         C   s   |  j  S(   s{   Get the setting of geo_enabled for this user.
    
        Returns:
          True/False if Geo tagging is enabled
        (   t   _geo_enabled(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetGeoEnabled5  s    c         C   s   | |  _  d S(   s�   Set the latest twitter.geo_enabled of this user.
    
        Args:
          geo_enabled:
            True/False if Geo tagging is to be enabled
        N(   R�   (   R   R>   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetGeoEnabled=  s    s/   The value of twitter.geo_enabled for this user.c         C   s   |  j  S(   s|   Get the setting of verified for this user.
    
        Returns:
          True/False if user is a verified account
        (   t	   _verified(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetVerifiedI  s    c         C   s   | |  _  d S(   s�   Set twitter.verified for this user.
    
        Args:
          verified:
            True/False if user is a verified account
        N(   R�   (   R   R?   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetVerifiedQ  s    s,   The value of twitter.verified for this user.c         C   s   |  j  S(   si   Get the setting of lang for this user.
    
        Returns:
          language code of the user
        (   t   _lang(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetLang]  s    c         C   s   | |  _  d S(   sr   Set twitter.lang for this user.
    
        Args:
          lang:
            language code for the user
        N(   R�   (   R   R@   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetLange  s    s(   The value of twitter.lang for this user.c         C   s   |  j  S(   s�   Get the setting of notifications for this user.
    
        Returns:
          True/False for the notifications setting of the user
        (   t   _notifications(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetNotificationsq  s    c         C   s   | |  _  d S(   s�   Set twitter.notifications for this user.
    
        Args:
          notifications:
            True/False notifications setting for the user
        N(   R�   (   R   RA   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetNotificationsy  s    s1   The value of twitter.notifications for this user.c         C   s   |  j  S(   s�   Get the setting of contributors_enabled for this user.
    
        Returns:
          True/False contributors_enabled of the user
        (   t   _contributors_enabled(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetContributorsEnabled�  s    c         C   s   | |  _  d S(   s�   Set twitter.contributors_enabled for this user.
    
        Args:
          contributors_enabled:
            True/False contributors_enabled setting for the user
        N(   R�   (   R   RB   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetContributorsEnabled�  s    s8   The value of twitter.contributors_enabled for this user.c         C   s   |  j  S(   sr   Get the setting of created_at for this user.
    
        Returns:
          created_at value of the user
        (   t   _created_at(   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   GetCreatedAt�  s    c         C   s   | |  _  d S(   s�   Set twitter.created_at for this user.
    
        Args:
          created_at:
            created_at value for the user
        N(   R�   (   R   RC   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   SetCreatedAt�  s    s.   The value of twitter.created_at for this user.c         C   s   |  j  | � S(   N(   R   (   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   �  s    c         C   sO  y6| o4|  j  | j  k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j	 | j	 k o4|  j
 | j
 k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k o4|  j | j k SWn t k
 rJt  SXd  S(   N(!   R   R   R   R)   R*   R+   R,   R-   R.   R/   R0   R1   R2   R3   R4   R5   R6   R7   R<   R:   R8   R;   R9   R=   R>   R?   R@   RA   RB   RC   RD   R   R   (   R   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   �  sF    c         C   s
   |  j  �  S(   s�   A string representation of this twitter.User instance.
    
        The return value is the same as the JSON string representation.
    
        Returns:
          A string representation of this twitter.User instance.
        (   R   (   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   �  s    c         C   s   t  j |  j �  d t �S(   s�   A JSON string representation of this twitter.User instance.
    
        Returns:
          A JSON string representation of this twitter.User instance
       R   (   R    R   R   R    (   R   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   �  s    c         C   s#  i  } |  j  r |  j  | d <n  |  j r8 |  j | d <n  |  j rQ |  j | d <n  |  j rj |  j | d <n  |  j r� |  j | d <n  |  j r� |  j | d <n  |  j r� |  j | d <n  |  j r� |  j | d <n  |  j d  k	 r� |  j | d	 <n  |  j
 r|  j
 | d
 <n  |  j r|  j | d <n  |  j r8|  j | d <n  |  j rQ|  j | d <n  |  j rj|  j | d <n  |  j r�|  j | d <n  |  j d  k	 r�|  j | d <n  |  j r�|  j | d <n  |  j r�|  j | d <n  |  j r�|  j | d <n  |  j r|  j j �  | d <n  |  j r%|  j | d <n  |  j r>|  j | d <n  |  j rW|  j | d <n  |  j rp|  j | d <n  |  j r�|  j | d <n  |  j r�|  j | d <n  |  j r�|  j | d <n  |  j r�|  j | d <n  |  j r�|  j | d <n  |  j r|  j | d <n  |  j  r|  j  | d <n  | S(!   s�   A dict representation of this twitter.User instance.
    
        The return value uses the same key names as the JSON representation.
    
        Return:
          A dict representing this twitter.User instance
        R   R   R   R)   R*   R+   R,   R-   R.   R/   R0   R1   R2   R3   R4   R5   R6   R7   R<   R=   R9   R8   R:   R;   R>   R?   R@   RA   RB   RC   RD   N(!   R   R   R   R)   R*   R+   R,   R-   R.   R	   R/   R0   R1   R2   R3   R4   R5   R6   R7   R<   R=   R   R9   R8   R:   R;   R>   R?   R@   RA   RB   RC   RD   (   R   R!   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR   �  s�    																													c      A   C   sm  d |  k r2 d d l  m } | j |  d � } n d# } t d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d	 |  j d	 d# � d
 |  j d
 d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d |  j d d# � � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d | d |  j d d# � d |  j d d# � d |  j d d# � d |  j d d# � d  |  j d  d# � d! |  j d! d# � d" |  j d" d# � � S($   s�   Create a new instance based on a JSON dict.
    
        Args:
          data:
            A JSON dict, as converted from the JSON in the twitter API
    
        Returns:
          A twitter.User instance
        R=   i����(   t   StatusR   R   R   R)   R*   R:   R8   R;   R+   R,   R9   R-   t   profile_image_url_httpsR.   R/   R0   R1   R2   R3   R4   R5   R6   R7   R<   R>   R?   R@   RA   RB   RC   RD   N(   t   twitterR�   R#   R	   R(   R   (   R!   R�   R=   (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR#   2  sF    (c   R$   R%   R&   R   RF   RG   t   propertyR   RJ   RK   R   R   RM   R   RO   RP   R)   RR   RS   R*   RU   RV   R<   RX   RY   R-   R[   R\   R.   R^   R_   R/   Ra   Rb   R0   Rd   Re   R1   Rg   Rh   R2   Rj   Rk   R3   Rm   Rn   R4   Rp   Rq   R5   Rs   Rt   R6   Rv   Rw   R7   Ry   Rz   R=   R|   R~   R9   R�   R�   RD   R�   R�   R8   R�   R�   R:   R�   R�   R;   R�   R�   R>   R�   R�   R?   R�   R�   R@   R�   R�   RA   R�   R�   RB   R�   R�   RC   R   R   R   R   R   R'   R#   (    (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyR(   �   s�   $	&																																																																																															&	
		JN(   R�   R    R   t   objectR   R(   (    (    (    s8   /Users/Samuel/Developer/python/hiroshima/twitter/user.pyt   <module>   s   ~