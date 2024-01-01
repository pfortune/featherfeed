<script>
    import { page } from '$app/stores';

    let detection = null;
    let errorMessage = '';

    $: loadDetection($page.params.id);

    async function loadDetection(id) {
        try {
            const response = await fetch(`https://api.featherfeed.ie/detection/${id}`);
            if (response.ok) {
                detection = await response.json();
            } else {
                errorMessage = `Failed to fetch detection: ${response.statusText}`;
            }
        } catch (error) {
            errorMessage = `Error fetching detection: ${error.message}`;
        }
    }

    function formatDate(dateString) {
        const options = { hour: '2-digit', minute: '2-digit', year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString(undefined, options);
    }

    function formatScientificName(genus, species) {
        return `${genus} ${species}`;
    }
</script>

{#if detection}
    <div class="container mx-auto p-4">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-3xl font-bold">{detection.common_name}</h2>
            <a href="/detections" class="text-blue-600 hover:text-blue-800 transition duration-300 ease-in-out">Back to List</a>
        </div>

        <div class="flex flex-wrap md:flex-nowrap">
            <!-- Left column for details -->
            <div class="w-full md:w-1/2 md:pr-4 mb-4">
                <p><strong>ID:</strong> {detection.id}</p>
                <p><strong>Date:</strong> {formatDate(detection.date)}</p>
                <p><strong>Common Name:</strong> {detection.common_name}</p>
                <p><strong>Scientific Name:</strong> {formatScientificName(detection.genus, detection.species)}</p>
                <p><strong>Temperature:</strong> {detection.temperature}°C</p>
                <p><strong>Humidity:</strong> {detection.humidity}%</p>
            </div>

           <!-- Right column for image -->
            {#if detection.imageref}
                <div class="w-full md:w-1/2">
                    <img src={detection.imageref} alt={`Image of ${detection.species}`} class="w-full h-auto rounded shadow" />
                </div>
            {/if}
        </div>

        <!-- Full-width video -->
        {#if detection.videoref}
            <div class="w-full mt-4">
                <strong>Video:</strong>
                <!-- svelte-ignore a11y-media-has-caption -->
                <video controls src={detection.videoref} class="w-full mt-2 rounded shadow">
                    Your browser does not support the video tag.
                </video>
            </div>
        {/if}
    </div>
{:else}
    <div class="container mx-auto p-4 text-center">
        {#if errorMessage}
            <p class="text-red-600">{errorMessage}</p>
        {:else}
            <p>Loading...</p>
        {/if}
    </div>
{/if}
