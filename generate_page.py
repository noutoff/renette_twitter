
before_posts = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"
        integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
        <link rel="icon" type="image/png" href="https://cdn-icons-png.flaticon.com/512/124/124021.png"/>
    <title>Renette and Charles (@renettethefrog) / Ribbitter</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp"
      rel="stylesheet">
      <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- sidebar starts -->
    <div class="sidebar">
      <!-- <i class="fab fa-twitter"></i> -->
      <img style="height: 30px; margin-left: 20px; margin-top:20px" src="images/frog-face.png">
        <div class="sidebarOption active">
            <span class="material-icons">home</span>
            <h2>Home</h2>
        </div>

        <div class="sidebarOption">
            <span class="material-icons">search</span>
            <h2>Explore</h2>
        </div>

        <div class="sidebarOption">
            <span class="material-icons">notifications</span>
            <h2>Notifications</h2>
        </div>

        <div class="sidebarOption">
            <span class="material-icons">chat</span>
            <h2>Message</h2>
        </div>

        <div class="sidebarOption">
            <span class="material-icons">bookmark</span>
            <h2>Bookmarks</h2>
        </div>

        <div class="sidebarOption">
            <span class="material-icons">list</span>
            <h2>List</h2>
        </div>

        <div class="sidebarOption">
            <span class="material-icons">person</span>
            <h2>Profile</h2>
        </div>

        <div class="sidebarOption">
            <span class="material-icons">more_horiz</span>
            <h2>More</h2>
        </div>

        <button id="btn-tweet">Ribbit</button>
    </div>
    <!-- sidebar ends -->

    <!-- feed starts -->
    <div class="feed">

      <!-- banner starts -->
      <div class="banner">
	<div class="banner_body">
	  <div class="banner-name">
	    Rennette and Charles
	  </div>
	  <div class="banner-tweets">
	    45297 Tweets
	  </div>
	  <img class="banner-img" src="images/frogcapy2.webp" alt="">
	</div>
      </div>
      <!-- banner ends -->

      <!-- profile starts -->
      <div class="profile">
	<div class="profile_body">
	  <img class="profile-avatar" src="./images/renette.jpg" alt="Renette" />
	  <div class="profile-name">
	    Renette and Charles
	    <div class="profile-at">
	      @renettethefrog
	    </div>
	  </div>
	  <div class="profile-info">
	    Just a frog and her capybara friend bonking the world.
	    Art by @baysalt and @silvanborer
	  </div>
	  <div class="profile-calendar">
	  <svg viewBox="0 0 24 24" aria-hidden="true" class="calendar-icon"><g><path d="M19.708 2H4.292C3.028 2 2 3.028 2 4.292v15.416C2 20.972 3.028 22 4.292 22h15.416C20.972 22 22 20.972 22 19.708V4.292C22 3.028 20.972 2 19.708 2zm.792 17.708c0 .437-.355.792-.792.792H4.292c-.437 0-.792-.355-.792-.792V6.418c0-.437.354-.79.79-.792h15.42c.436 0 .79.355.79.79V19.71z"></path><circle cx="7.032" cy="8.75" r="1.285"></circle><circle cx="7.032" cy="13.156" r="1.285"></circle><circle cx="16.968" cy="8.75" r="1.285"></circle><circle cx="16.968" cy="13.156" r="1.285"></circle><circle cx="12" cy="8.75" r="1.285"></circle><circle cx="12" cy="13.156" r="1.285"></circle><circle cx="7.032" cy="17.486" r="1.285"></circle><circle cx="12" cy="17.486" r="1.285"></circle></g></svg>
	  Joined Desnus 7172 AM
	  </div>
	  <div class="profile-following">
	    <b style="color:black">1827</b> Following <b style="color:black; margin-left:20px">12</b> Followers
	  </div>
	  <nav>
        <a href="" class="active"><div style="padding-top:16px; padding-bottom:16px">Tweets<div class="blue-thingy"></div></div></a>
        <a href=""><div style="padding-top:16px; padding-bottom:16px">Tweets and replies</div></a>
        <a href=""><div style="padding-top:16px; padding-bottom:16px">Medias</div></a>
	<a href=""><div style="padding-top:16px; padding-bottom:16px">Likes</div></a>
      </nav>
	</div>
      </div>

      <!-- profile ends -->
"""

after_posts = """
   </div>
    <!-- feed ends -->
    <!-- widget starts -->
    <div class="widget">
        <div class="widget-search-bar">
            <span class="material-icons">
                search
                </span>
            <input type="text" id="widget-search-bar-input" value="" placeholder="Search twitter">
        </div>

	<div class="widget-container">
	  <h3> You might know </h3>
	  <div class="who">
	   <ul>
             <li>
               <div class="profile">
                 <div class="info">
		   <img src="./images/kant.png" alt="Avatar" />
                   <div><strong>Kant Trus<br> <span>@kanttrusthenotcat</span></strong></div>
                 </div>
		 <div><button>Follow</button></div>
               </div>
             </li>
             <li>
               <div class="profile">

                 <div class="info">
		   <img src="images/jacques.png" alt="Avatar" />
                   <strong>Jaques Desorteils <br><span>@jaquesfrostbite</span></strong>
                 </div>
		 <div><button>Follow</button></div>
               </div>
             </li>
             <li>
               <div class="profile">

                 <div class="info">
		   <img src="images/rizzie.png" alt="Avatar" />
                   <strong>Rizzie<br><span>@rizziethewitch</span></strong>
                 </div>
		 <div><button>Follow</button></div>
               </div>
             </li>
           </ul>
	   </div>
	</div>

        <div class="widget-container">
          <h3><b>Trends for you</b></h3>
	  <div class="trend">
	  <ul>
            <li><span>#OrcCityForstBite</span></li>
            <li><span>#eatenbyagiantmosquito</span></li>
            <li><span>#Temperateforlife</span></li>
            <li><span>#isawsarenrae</span></li>
	    <li><span>#themostdangerousgame</span></li>
          </ul>
	  </div>
        </div>

    </div>
    <!-- widget ends -->

</body>
</html>
"""

post_template = """
      <div class="post">
        <div class="post-avatar">
          <img src="images/renette.jpg" alt="">
        </div>
        <div class="post_body">
          <div class="post-header">
            <div class="post-header-username">
              Renette and Charles
              <span class="post-header-icon">
                <span class="material-icons">verified</span>@renettethefrog · {date}
              </span>
            </div>
          </div>
          <div class="post-description">
            {text}
          </div>
          {img}
          <div class="post-options">

	  </div>
	  <div class="actions">
            <a href=""><img src="./images/chat-round.svg" alt="Comments" /> 101</a>
            <a href=""><img src="./images/refresh-69.svg" alt="Retweet" /> 59</a>
            <a href=""><img src="./images/heart-2.svg" alt="Like" /> 25</a>
            <a href=""><img src="./images/email-83.svg" alt="Email" /> 13</a>
          </div>
        </div>
      </div>
"""

post_image_template = """
<img class="post-image" src="{img_src}" alt="">
"""


posts = [
    ("Hi! I'm Renette Bloux Dubonk and I was just born today!", "Desnus 23, 7172 AM", ""),
    ('One of the grown-up gave me a big stick so I could start "learning the way of the bonk", whatever that means', "Calistril 28 7175 AM", ""),
    ("I've bonked things for a few months now, it's pretty fun. Now I have to sit through theoretical bonk lessons. I'm learning about the different style of bonking: melee bonking (very traditional), range bonking, magic bonking... It's pretty interesting!", "Neth 13, 7175 AM", ""),
    ("My cousin Zoe Dabonk came to visit today, we had so much fun! She's a bit older so she's clearly more advanced in her bonk studies, but she still took the time to show me some stuff! She also told me scary stories about a moss witch leaving in the jungle that hates noise...", "Abadius 22, 7177 AM", "images/frogs.jpg"),
    ("I've started going with the grown-ups on bonking expeditions! It's when we go in the jungle to bonk things so that they leave the village alone. I only bonked small creatures but it was nice getting some actual action!", "Gozran 4, 7179 AM", ""),
    ("The others gave me a new bonking stick! It's a very good stick, I'll call it Maximo.", "Rova 14, 7179 AM", "images/hammer.webp"),
    ("They keep saying that I need to find my bonking style, but I don't really now what to do. I can sense there's something missing. But what? Leaf got her dancing bonk, Olive got their random magic bonk, and all I got is Maximo... (sorry Maximo you're cool)", "Abadius 19, 7180 AM", ""),
    ("Wow something incredible happened!!! I was", "Sarenith 15, 7180 AM", ""),
    ("Sorry I was excited and sent to early. I was picking cool rocks for my collection (Hector is lonely), when I heard distressed noise in the bushes. A poor capybara was being attacked by a weird thing with lots of limbs (way too many limbs). Thankfully I had Maximo with me so I started bonking, traditional melee style. But then! The capybara just pushed me with his head so that I would fall on him, and two seconds later I was riding him!! And we charged!!! That was so cool.", "Sarenith 15, 7180 AM", ""),
    ("So I came back to the village on the capybara and asked Josie to talk with him (she bonks using nature), and he said his name was Charles and that he thought we were making a great team and that he would love to continue bonking with me! So now I'm mounted bonking, wow!", "Sarenith 16, 7180 AM", "images/charles.jpg"),
    ("Bonking with Charles is so fun! But I feel like we need to travel a bit, witness other bonking styles, or maybe even... other things than bonking?? (we've heard of some Dubonks going into sports?) In any case we're super excited to go on an adventure together!", "Lamashan 2, 7183 AM", ""),
    ("Well here we are in a very cool adventure! We were hired by a pirate lady to compete in a game against other... people? I'm not sure I got all the details but it sounds fun!", "Pharast 12, 7184 AM", ""),
    ("I'm working with a really cool kitty-person named Kant Trus, she's so smart and she likes money! Apparently her style is to miss a lot and then BOOM, hit very hard!", "Lamashan 2, 7183 AM", ""),
    ("We've met with another team (I think we need to make friends with them?), they look really good! One of them looks familiar... and the other has a big cat!! And I think they knew the Dubonk name? So nice that the Order of the Bonk is so popular! I need to ask them what their style is!", "Lamashan 2, 7183 AM", ""),
]

if __name__ == "__main__":
    html_src = before_posts
    for text, date, img in posts:
        if img:
            html_src += post_template.format(text=text, img=post_image_template.format(img_src=img), date=date)
        else:
            html_src += post_template.format(text=text, img=img, date=date)
    html_src += after_posts
    with open("index.html", "w") as f:
        f.write(html_src)
