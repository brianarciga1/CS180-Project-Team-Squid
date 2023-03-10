<!--THIS IS FOR THE HOME PAGE!!!!-->
<template>
    <div class="Home">
      <strong class="font1"> CONGRATULATIONS!</strong>
      <p class="font2">Your new Spotify playlist has been created!</p>
      <nav>
        <RouterLink to="/">Home</RouterLink>
    </nav>
      <p class="font3"> THANK___YOU___FOR___USING<br>
        <div class="center">
        <img src="@/assets/images/Font.png" alt="centered image" style="max-width: 60%;">
      </div>
    </p>
      <div class="spacer"></div>
      <div class="center">
        <img src="@/assets/images/e39.png" alt="centered image" style="max-width: 14%; float: right;">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
    props: {
      msg: String
    }
  }
  </script>
  
  <style scoped>
  
  @font-face {
    font-family: "Naruto";
    src: url(@/assets/fonts/NinjaNaruto-YOn4.ttf);
  }
  
  .center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 10vh;
    margin-bottom: 100px;
  }
  
  .spacer {
    height: 50px; /* adjust as needed */
  }
  
  .font1 {
    font-family: "Naruto", sans-serif;
    font-size: 70px;
    text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
    border: 10px solid rgba(199, 3, 166, 0.322);
    border-radius:10px;
    background-color: rgba(199, 3, 166, 0.452);
  }
  .font2 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 40px;
    font-weight: bold;
    text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
  }
  .font3 {
    font-family: "Naruto", sans-serif;
    font-size: 40px;
    text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
  }
  .font4 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;
    font-weight: bold;
    text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
  }
  nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

/*Changes color of text of current page*/
nav a.router-link-exact-active {
  color: orange;
  border: 10px solid orange;
}

/*This changes the color of the background of the current page you are on in the menu*/
nav a.router-link-exact-active:hover {
  background-color: purple;
  border: 10px solid purple;
}

/*Lets menu be side by side and changes border width and color*/
nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid white;
}

nav a:first-of-type {
  border: 1;
}

  </style>