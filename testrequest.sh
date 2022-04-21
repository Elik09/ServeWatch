#! /bin/bash
tamper="<script>alert(1)</script>"
hash=$RANDOM
messageblock="{\"id\":\"$hash\",\"machine\":\"machine\",\"user\":\"test\",\"action\":\"message\",\"file\":\"$tamper\",\"timestamp\":\"220315160405\"}"


# echo $messageblock
echo "curl -X POST -d '$messageblock' \"http://localhost:5000/submit/logs\""
