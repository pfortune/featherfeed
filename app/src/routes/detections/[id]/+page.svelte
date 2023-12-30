<script context="module">
    export async function load({ params }) {
        const res = await fetch(`https://api.featherfeed.ie/detections/${params.id}`);
        const detection = await res.json();
        return { props: { detection } };
    }
</script>

<script>
    export let detection;
</script>

<article>
    <h1>Detection Details</h1>
    <p><strong>Date:</strong> {detection.date}</p>
    <p><strong>Species:</strong> {detection.species}</p>
    <p><strong>Temperature:</strong> {detection.temperature}°C</p>
    <p><strong>Humidity:</strong> {detection.humidity}%</p>
    <video controls>
        <source src={detection.videoref} type="video/mp4">
        <track kind="captions" src="path_to_caption_file.vtt" srclang="en" label="English">
        Your browser does not support the video tag.
    </video>    
</article>
