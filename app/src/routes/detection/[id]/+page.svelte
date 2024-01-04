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
		const options = {
			hour: '2-digit',
			minute: '2-digit',
			year: 'numeric',
			month: 'long',
			day: 'numeric'
		};
		return new Date(dateString).toLocaleDateString(undefined, options);
	}

	function formatScientificName(genus, species) {
		return `${genus} ${species}`;
	}
</script>

{#if detection}
	<div class="container mx-auto p-4">
		<div class="flex justify-between items-center mb-6">
			<h2 class="text-4xl font-bold text-indigo-800">
				{detection.common_name}
			</h2>
			<a
				href="/detections"
				class="inline-flex items-center bg-blue-600 hover:bg-blue-800 text-white hover:shadow-lg rounded px-4 py-2"
			>
				<i class="fas fa-arrow-left mr-2" /> Back to List
			</a>
		</div>

		<div class="flex flex-wrap md:flex-nowrap gap-4">
			<!-- Left column for details -->
			<div class="w-full md:w-1/2 bg-white p-4 rounded-lg shadow">
				<table class="min-w-full">
					<tbody class="text-gray-700">
						<tr>
							<td><i class="fas fa-fingerprint" /> ID:</td>
							<td>{detection.id}</td>
						</tr>
						<tr>
							<td><i class="fas fa-calendar-alt" /> Date:</td>
							<td>{formatDate(detection.date)}</td>
						</tr>
						<tr>
							<td><i class="fas fa-dove" /> Common Name:</td>
							<td>{detection.common_name}</td>
						</tr>
						<tr>
							<td><i class="fas fa-dna" /> Scientific Name:</td>
							<td>{formatScientificName(detection.genus, detection.species)}</td>
						</tr>
						<tr>
							<td><i class="fas fa-thermometer-half" /> Temperature:</td>
							<td>{detection.temperature}°C</td>
						</tr>
						<tr>
							<td><i class="fas fa-tint" /> Humidity:</td>
							<td>{detection.humidity}%</td>
						</tr>
					</tbody>
				</table>
			</div>

			<!-- Right column for image -->
			{#if detection.imageref}
				<div class="w-full md:w-1/2 bg-white p-4 rounded-lg shadow flex justify-center">
					<img
						src={detection.imageref}
						alt={`Image of ${detection.species}`}
						class="w-auto h-64 rounded-lg"
					/>
				</div>
			{/if}
		</div>

		<!-- Full-width video -->
		{#if detection.videoref}
			<div class="w-full mt-4 bg-gray-100 p-4 rounded-lg shadow">
				<h3 class="text-xl font-semibold flex items-center mb-2">
					<i class="fas fa-video mr-2" /> Video
				</h3>
				<!-- svelte-ignore a11y-media-has-caption -->
				<video controls src={detection.videoref} class="w-full rounded">
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

<style>
	table {
		border-collapse: collapse;
		width: 100%;
	}

	td {
		padding: 8px;
		text-align: left;
		border-bottom: 1px solid #ddd;
	}

	tr:hover {
		background-color: #f5f5f5;
	}

	i {
		margin-right: 8px;
		color: #4a90e2; /* or any color you prefer */
	}

	.large-bird-image {
		border-radius: 15px;
	}
</style>
