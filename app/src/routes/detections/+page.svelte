<script>
    // Import necessary modules
    import { onMount, onDestroy } from 'svelte';
    import { createClient } from '@supabase/supabase-js';
    import { goto } from '$app/navigation';

    // Initialize Supabase client
    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
    const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;
    const supabase = createClient(supabaseUrl, supabaseAnonKey);

    let detections = [];
    let changesSubscription;

    onMount(async () => {
        await loadInitialData();

        // Subscribe to INSERT events on the public schema
        changesSubscription = supabase
            .channel('schema-db-changes')
            .on('postgres_changes', { event: 'INSERT', schema: 'public' }, (payload) => {
                // Filter for changes to the 'detections' table
                if (payload.table === 'detections') {
                    detections = [payload.new, ...detections];
                }
            })
            .subscribe();
    });

    async function loadInitialData() {
        const response = await fetch('https://api.featherfeed.ie/detections');
        if (response.ok) {
            detections = await response.json();
        }
    }

    function viewDetails(id) {
        goto(`/detection/${id}`);
    }

    function formatDate(dateString) {
        const options = { hour: '2-digit', minute: '2-digit', year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString(undefined, options);
    }
</script>


<div class="px-4 mt-10 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-xl font-semibold leading-6 text-gray-900">Bird Detections</h1>
        <p class="mt-2 text-sm text-gray-700">A list of all bird detections including date, species, temperature, and humidity.</p>
      </div>
    </div>
    <div class="-mx-4 mt-8 sm:-mx-6 lg:mx-0">
      <table class="min-w-full divide-y divide-gray-300">
        <thead class="bg-gray-50">
          <tr>
            <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Date</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 lg:table-cell">Species</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 sm:table-cell">Temperature</th>
            <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Humidity</th>
            <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
              <span class="sr-only">View</span>
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 bg-white">
          {#each detections as detection}
          <tr>
            <td class="w-full max-w-0 py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:w-auto sm:max-w-none sm:pl-0">
              {formatDate(detection.date)}
              <dl class="font-normal lg:hidden">
                <dt class="sr-only">Species</dt>
                <dd class="mt-1 truncate text-gray-700">{detection.common_name}</dd>
                <dt class="sr-only">Temperature</dt>
                <dd class="mt-1 truncate text-gray-500">{detection.temperature}°C</dd>
                <dt class="sr-only">Humidity</dt>
                <dd class="mt-1 truncate text-gray-500">{detection.humidity}% Humidity</dd>
              </dl>
            </td>
            <td class="hidden px-3 py-4 text-sm text-gray-500 lg:table-cell">{detection.common_name}</td>
            <td class="hidden px-3 py-4 text-sm text-gray-500 sm:table-cell">{detection.temperature}°C</td>
            <td class="px-3 py-4 text-sm text-gray-500">{detection.humidity}%</td>
            <td class="py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                <button  on:click={() => viewDetails(detection.id)} type="button" class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">View</button></td>
          </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
  