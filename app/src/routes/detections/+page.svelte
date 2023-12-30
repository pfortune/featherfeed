<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';

    let detections = [];

    onMount(async () => {
        const response = await fetch('https://api.featherfeed.ie/detections');
        if (response.ok) {
            detections = await response.json();
        }
    });

    function viewDetails(id) {
        goto(`/detections/${id}`);
    }
</script>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Date</th>
            <th>Species</th>
            <th>Temperature</th>
            <th>Humidity</th>
            <th>View</th>
        </tr>
    </thead>
    <tbody>
        {#each detections as detection}
            <tr>
                <td>{detection.id}</td>
                <td>{detection.date}</td>
                <td>{detection.species}</td>
                <td>{detection.temperature}°C</td>
                <td>{detection.humidity}%</td>
                <td>
                    <button on:click={() => viewDetails(detection.id)}>Details</button>
                </td>
            </tr>
        {/each}
    </tbody>
</table>
