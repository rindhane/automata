import './App.css';
import Playground from './Components/playground/playground';
import {NodeMapProvider} from './Contexts/nodemap.js';


function App() {
  return (
    <div className='App'>
      <NodeMapProvider>
      <div className='Header'></div>
      <Playground />
      <div className='Footer'></div>
      </NodeMapProvider>
    </div>
  );
}

export default App;
