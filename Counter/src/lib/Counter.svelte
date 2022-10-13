<script>
  let count = 0
  const increment = () => {
    count += 1
  }
</script>

<div>
  <button on:click={increment}>Click Me</button>
<p id="clickedNum">You have clicked the button {count} times.</p>
</div>

