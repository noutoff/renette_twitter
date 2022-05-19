

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
		   <img src="images/frog-face.png" alt="Avatar" />
                   <strong>Jaques Desorteils <br><span>@jaquesfrostbite</span></strong>
                 </div>
		 <div><button>Follow</button></div>
               </div>
             </li>
             <li>
               <div class="profile">

                 <div class="info">
		   <img src="images/frog-face.png" alt="Avatar" />
                   <strong>Goblinwitch<br><span>@thegoblinwitch</span></strong>
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
                <span class="material-icons">verified</span>@renettethefrog
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
    ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", ""),
    ("hello hello", "images/frogcapy.webp"),
    ("hello again", ""),
    ("Hey I was born! Look at that!", "")
]

# TODO: add dates!

if __name__ == "__main__":
    html_src = before_posts
    for text, img in posts:
        if img:
            html_src += post_template.format(text=text, img=post_image_template.format(img_src=img))
        else:
            html_src += post_template.format(text=text, img=img)
    html_src += after_posts
    with open("index.html", "w") as f:
        f.write(html_src)