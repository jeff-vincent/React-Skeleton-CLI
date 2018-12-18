import React from 'react';
import './genericComponent.css'

class genericComponent extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
      return (
         <div className="row">
             <div>
                 Your content goes here. 
             </div>    
         </div>
      );
   }
}

export default genericComponent;