---
layout: home
title: Football Specials Coffee Shop
---

<style>
  img#footballLogo {
    width: 300px !important;
    height: auto !important;
    max-width: 100%;
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

<img id="footballLogo" src="Football_specials_logo.jpg" alt="Football Specials Coffee Shop">

Welcome to **Casuals Coffee Shop** — explore our blog posts below!
