<script context="module">
    export async function load({ params, fetch }) {
        try {
            console.log(`Fetching detection with ID: ${params.id}`);
            const res = await fetch(`https://api.featherfeed.ie/detections/${params.id}`);
            if (res.ok) {
                const detection = await res.json();
                return { props: { detection } };
            } else {
                console.error('Failed to fetch detection:', res.statusText);
                return { props: { detection: null } };
            }
        } catch (error) {
            console.error('Error:', error);
            return { props: { detection: null } };
        }
    }
</script>

<script>
    export let detection;
    console.log(detection);
</script>

{#if detection}
    <article class="max-w-2xl mx-auto my-8 p-6 bg-white shadow-lg rounded-md">
        <h1 class="text-2xl font-bold text-gray-800 mb-4">Detection Details</h1>
        <p class="mb-2"><strong class="text-gray-700">Date:</strong> {detection.date}</p>
        <p class="mb-2"><strong class="text-gray-700">Species:</strong> {detection.species}</p>
        <p class="mb-2"><strong class="text-gray-700">Temperature:</strong> {detection.temperature}°C</p>
        <p class="mb-4"><strong class="text-gray-700">Humidity:</strong> {detection.humidity}%</p>
        <div class="mb-4">
            <video controls class="w-full">
                <source src={detection.videoref} type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        <img src={detection.imageref} alt={`Image of ${detection.species}`} class="w-full h-auto" />
    </article>
{:else}
    <p class="text-center my-8 text-xl text-gray-700">Detection details not available.</p>
{/if}
