import React from 'react'
import Display from './Display'

function Interface(props) {

    const buttons_info = [
        {text: "(", color: "#cccccc", handler: () => props.buttonHandler("bracket", "(")}, 
        {text: ")", color: "#cccccc", handler: () => props.buttonHandler("bracket", ")")},
        {text: "%", color: "#cccccc", handler: () => props.buttonHandler("percentage", "")}, 
        {text: "CE", color: "#cccccc", handler: () => props.buttonHandler("clear", "")},
        {text: "7", color: "#eeeeee", handler: () => props.buttonHandler("number", 7)}, 
        {text: "8", color: "#eeeeee", handler: () => props.buttonHandler("number", 8)}, 
        {text: "9", color: "#eeeeee", handler: () => props.buttonHandler("number", 9)}, 
        {text: "/", color: "#cccccc", handler: () => props.buttonHandler("operation", " / ")}, 
        {text: "4", color: "#eeeeee", handler: () => props.buttonHandler("number", 4)}, 
        {text: "5", color: "#eeeeee", handler: () => props.buttonHandler("number", 5)},
        {text: "6", color: "#eeeeee", handler: () => props.buttonHandler("number", 6)},
        {text: "*", color: "#cccccc", handler: () => props.buttonHandler("operation", " x ")}, 
        {text: "1", color: "#eeeeee", handler: () => props.buttonHandler("number", 1)},
        {text: "2", color: "#eeeeee", handler: () => props.buttonHandler("number", 2)},
        {text: "3", color: "#eeeeee", handler: () => props.buttonHandler("number", 3)},
        {text: "-", color: "#cccccc", handler: () => props.buttonHandler("operation", " - ")},
        {text: "0", color: "#eeeeee", handler: () => props.buttonHandler("number", "0")},
        {text: ".", color: "#eeeeee", handler: () => props.buttonHandler("dot", ".")},
        {text: "=", color: "#89cff0", handler: () => props.buttonHandler("equal", "")},
        {text: "+", color: "#cccccc", handler: () => props.buttonHandler("operation", " + ")},
    ];

    const buttons = buttons_info.map((button) => {
        return (
            <button className="panel-button" style={{background: button.color}} onClick={button.handler}>
                {button.text}
            </button>
        );
    }) 

    return(
        <div className="interface">
            <Display displayValue={props.displayValue}></Display>
            {buttons}
        </div>
      );
}

export default Interface