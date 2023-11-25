<script>
  import { onMount } from 'svelte';

  let statusMessage = 'Loading...';

  onMount(async () => {
    try {
      const response = await fetch('http://localhost:3000/status');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      statusMessage = data.status;
    } catch (error) {
      console.error('Error fetching status:', error);
      statusMessage = 'Error fetching status';
    }
  });
</script>

<h1>API Status: {statusMessage}</h1>
