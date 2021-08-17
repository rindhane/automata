import './App.css';
import Playground from './Components/playground/playground';
import {NodeMapProvider} from './Contexts/nodemap.js';
import  {Header} from './Components/headers/headers.js';

function App() {
  return (
    <div className='App'>
      <NodeMapProvider>
      <Header/>
      <div className='Playground'><Playground /> </div>
      <div className='Footer'></div>
      </NodeMapProvider>
    </div>
  );
}

export default App;
