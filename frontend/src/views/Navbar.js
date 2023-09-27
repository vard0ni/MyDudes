import React, {useContext} from 'react'
import jwt_decode from "jwt-decode";
import AuthContext from "../context/AuthContext";
import {Link} from "react-router-dom";

function Navbar() {

    const {user, logoutUser} = useContext(AuthContext)
  const token = localStorage.getItem("authTokens")

  if (token){
    const decoded = jwt_decode(token)
    var user_id = decoded.user_id
  }

    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">
                        <h3>mydudes</h3>

                    </a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                            data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false"
                            aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav ">
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="#">Home</a>
                            </li>
                            {token === null &&
                                <>
                                    <li className="nav-item">
                                        <Link class="nav-link" to="/login">Login</Link>
                                    </li>
                                    <li className="nav-item">
                                        <Link class="nav-link" to="/register">Register</Link>
                                    </li>
                                </>
                            }

                            {token !== null &&
                                <>
                                    <li className="nav-item">
                                        <a className="nav-link" href="/dashboard">Dashboard</a>
                                    </li>
                                    <li className="nav-item">
                                        <a className="nav-link" onClick={logoutUser}
                                           style={{cursor: "pointer"}}>Logout</a>
                                    </li>
                                </>
                            }

                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default Navbar
