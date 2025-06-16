---
layout: home
title: Casuals Coffee Shop
---

<style>
  #logo {
    width: 300px;
    height: auto;
    margin: 20px 0;
    display: block;
  }
</style>

<nav>
  <select id="categorySelect" onchange="navigateToCategory()">
    <option value="">-- Select Category --</option>
    <option value="art.html">Art</option>
    <option value="music.html">Music</option>
    <option value="football.html">Football</option>
  </select>
</nav>

<script>
  function navigateToCategory() {
    const page = document.getElementById("categorySelect").value;
    if (page) {
      window.location.href = page;
    }
  }
</script>

<img id="logo" src="Football_specials_logo.jpg" alt="Site logo">

<p>Welcome — explore our blog posts below!</p>

