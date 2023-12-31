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
                    detections = [...detections, payload.new];
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


<div class="overflow-x-auto">
    <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
            <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Date
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Species
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Temperature
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Humidity
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    View
                </th>
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
            {#each detections as detection}
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {formatDate(detection.date)}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {detection.species}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {detection.temperature}°C
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {detection.humidity}%
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                        <button  on:click={() => viewDetails(detection.id)} type="button" class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">More Details</button>
                    </td>                    
                </tr>
            {/each}
        </tbody>
    </table>
</div>
