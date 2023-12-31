<!-- Assuming this is in your layout file -->
<script>
  import "../app.css";
</script>

<nav class="bg-blue-400">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <div class="flex-shrink-0">
          <img src="logo.png" alt="Feather Feed Logo" class="mx-auto h-20 w-auto" />
        </div>
        <div class="hidden md:block">
          <div class="ml-10 flex items-baseline space-x-4">
            <!-- Navigation Links -->
            <a href="/" class="text-black-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</a>
            <a href="/detections" class="text-black-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Detections</a>
            <a href="https://github.com/pfortune/FeatherFeed" target="_blank" class="text-black-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">GitHub</a>
          </div>
        </div>
      </div>
      <!-- Mobile menu button -->
      <div class="-mr-2 flex md:hidden">
        <!-- Menu button omitted for brevity -->
      </div>
    </div>
  </div>

  <!-- Mobile menu, show/hide based on menu state. Omitted for brevity -->
</nav>

<slot />
