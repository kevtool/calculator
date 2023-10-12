import React from 'react'

function Display(props) {

    return(
        <div className="display">
            {props.displayValue}
        </div>
      );
}

export default Display