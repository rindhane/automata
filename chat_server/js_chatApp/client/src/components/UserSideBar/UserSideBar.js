import React from 'react';
import './UserSideBar.css';

const UserSideBar = ({users})=> {
    return (
        <div >
            <div className="topBar">
                <h3 style={{ textAlign: 'center' }}> Users Logged In</h3>
            </div>
            <div className="userContainer">
                <ul>
                    {users.map((user,i)=>{
                        return (
                            <li key={i}>{user}</li>
                            );
                    })
                    }
                </ul>
            </div>
        </div>
    );
    
};

export default UserSideBar;