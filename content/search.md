---
title: "Search"
layout: "search"
summary: "Search OSArch"
placeholder: "Search posts, pages, and events"
draft: false
---

<script>
window.addEventListener("load", function () {
  const query = new URLSearchParams(window.location.search).get("q");
  const input = document.getElementById("searchInput");
  if (!query || !input) return;

  const run = function () {
    if (input.disabled) return false;
    input.value = query;
    input.dispatchEvent(new Event("input", { bubbles: true }));
    return true;
  };

  let attempts = 0;
  const timer = window.setInterval(function () {
    attempts += 1;
    if (run() || attempts > 40) {
      window.clearInterval(timer);
    }
  }, 100);
});
</script>
