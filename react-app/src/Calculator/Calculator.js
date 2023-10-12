import React, { useState, useEffect }  from 'react'
import Interface from './Interface'
import reactStringReplace from 'react-string-replace';

function Calculator(props) {

    const [displayStr, setDisplayStr] = useState("0");
    const [bracketCount, setBracketCount] = useState(0);
    const [state, setState] = useState(["clear"]);

    function keyDown(event){
        let key = event.key;
        switch(key){
            case "Backspace":
                backward();
                break;
        }
    }

    useEffect(() => {
        document.addEventListener("keydown", keyDown);
        return () => document.removeEventListener("keydown", keyDown);
    });

    useEffect(() => {
        console.log(state)
    }, [state]);

    function displayInput(str){
        if (state.at(-1) === "equal" && (str !== " + " && str !== " - " && str !== " x " && str !== " / ")){
            setDisplayStr(str.toString())
        } else if (state.at(-1) === "clear" && str === " - "){
            setDisplayStr("-")
        } else if (state.at(-1) === "clear" && (str !== " + " && str !== " x " && str !== " / ")){
            setDisplayStr(str.toString())
        } else {
            setDisplayStr(displayStr + str.toString())
        }
    }

    function backward(){
        if (state.length > 1){
            setState(state.slice(0, state.length - 1))
        }

        if (displayStr.length == 1){
            setDisplayStr('0')
            return
        }
        var str = displayStr
        if (displayStr[displayStr.length - 1] == ' '){
            setDisplayStr(displayStr.slice(0, displayStr.length - 3))
        } else {
            setDisplayStr(displayStr.slice(0, displayStr.length - 1))
        }
    }

    function replaceOperation(newOperation){
        var str = displayStr.slice(0, displayStr.length - 3)
        setDisplayStr(str + newOperation)
    }

    function calculate(){
        var argStr = displayStr;
        argStr = reactStringReplace(argStr, '+', () => (
            "%2B"
        ));
        argStr = argStr.map((str) => str).join('');
        console.log(argStr)

        fetch("/calculate?str=" + argStr, {
            method: "GET",
        }).then((res) =>
            res.json().then((data) => {
                setDisplayStr(data.result);
            })
        );
    }
    
    function buttonHandler(type, value){
        if (type === "number"){
            displayInput(value);

            if (state.at(-1) === "dot" || state.at(-1) === "numDot"){
                setState([ ...state, "numDot"]);
            } else {
                console.log("hi")
                setState([ ...state, "number"]);
            }

        } else if (type === "dot" && state.at(-1) !== "dot" && state.at(-1) !== "numDot"){
            displayInput(value);
            setState([ ...state, "dot"]);
        } else if (type === "operation"){

            if (state.at(-1) === "operation"){
                replaceOperation(value);
            } else if (state.at(-1) === "clear" && value === " - "){
                displayInput(value);
                setState([ ...state, "negative"]);
            } else if (state.at(-1) !== "bracket_left"){
                displayInput(value);
                setState([ ...state, "operation"]);
            }
            
        } else if (type === "bracket"){
            if (value === "("){
                setBracketCount(bracketCount + 1);
                displayInput(value);
                setState([ ...state, "bracket_left"]);
            } else if (bracketCount > 0){
                setBracketCount(bracketCount - 1); 
                displayInput(value);
                setState([ ...state, "bracket_right"]);
            }
        } else if (type === "clear"){
            setDisplayStr("0");
            setState(["clear"]);
        } else if (type === "equal"){
            calculate();
            setState(["equal"]);
        }
    }

    return (
        <>
            <Interface buttonHandler={buttonHandler} displayValue={displayStr}/>
        </>
      );
}

export default Calculator