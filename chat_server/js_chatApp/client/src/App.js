import React from 'react';
import {BrowserRouter as Router, Route, Redirect} from 'react-router-dom';
import Join from './components/Join/Join';
import Chat from './components/Chat/Chat';
import Verify from './components/Verify/Verify';
import useLocalStorage from './hooks/useLocalStorage';
import { SocketProvider } from './context/socketProvider';
import {useFirebase} from './context/firebaseProvider';

const App = () => {
  const [mId,setMid]=useLocalStorage('mId');
  return(
    <Router>
      <Route path="/" exact >
        { mId ? <Redirect to= "/chat" /> :<SocketProvider mId={mId}><Join onSetId={setMid} mId={mId}/></SocketProvider> }
      </Route>
      <Route path="/chat" exact > 
        {mId ?  <SocketProvider mId={mId}><Chat mId={mId} setMid={setMid}/></SocketProvider> : < Redirect to="/" /> }
      </Route>
      <Route path="/verify" exact render={(props)=>(
                                         <SocketProvider mId={mId}> 
                                            <Verify mId={mId} setId={setMid} {...props}/>
                                          </SocketProvider>
                                          )} />
    </Router>
  )   
};

export default App;
