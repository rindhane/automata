import './App.css';
import Node from './Components/node/node.js'



function App() {
  return (
    <div>
    <Node title='Box' index='1' top='0'/>
    <Node title='Box ' index = '2' 
          message='just additional box'
          top = '100'
          />
    </div>
  );
}

export default App;
