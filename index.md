---
layout: home
title: Casuals Coffee Shop
---

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

Welcome to **Casuals Coffee Shop** — explore our blog posts below!
