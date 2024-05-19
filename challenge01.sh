#!/bin/bash

animate_text() {
    text="$1"
    delay="$2"
    for (( i=0; i<${#text}; i++ )); do
        echo -n "${text:$i:1}"
        sleep "$delay"
    done
    echo
}

animate_text "HaadLC - CTF | Second Challenge" 0.06 
animate_text "We will test how attentive you are. Be careful" 0.06

echo -e "\nPrompt:"
echo -e "You have certainly watched the movie 'Matrix'. If you haven't, hurry up. You are now led by Neo's lover, the flag is on Neo's lover."

echo -e "\nAccepted Commands That You Must Use:"
echo -e "ls | cd | cat | grep | mkdir | touch "
