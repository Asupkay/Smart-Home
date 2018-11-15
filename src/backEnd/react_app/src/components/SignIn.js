import React,{Component} from 'react';
import {withRouter} from 'react-router-dom';
import firebase from './firebase';

const SignInPage = ({ history }) =>
<div>
<h1>SignIn</h1>
<SignInForm history={history} />
</div>

const byPropKey = (propertyName, value) => () => ({
    [propertyName]: value,
});

const INITIAL_STATE = {
    email: '',
    password: '',
    error: null,
};

class SignInForm extends Component {
    constructor(props) {
        super(props);
        this.state = { ...INITIAL_STATE };


    }
    onSubmit = (event) => {
        event.preventDefault();
        const db = firebase.firestore();
        var citiesRef = db.collection('homes');
        var query = citiesRef.where('homeID', '==', this.state.email).where('password','==',this.state.password);
        var observer = query.onSnapshot(querySnapshot => {
            if (querySnapshot.size == 1){
                this.props.history.push("/");
            }
            else{
                this.props.history.push("/signIn");
            }
          });

        /* add date in firebase database
        const userRef = db.collection("home").add({
            homeID: this.state.email,
            password: this.state.password
        });*/
        this.setState({
            email: "",
            password: ""
        });
    }

    render() {
        const {
            email,
            password,
            error,
        } = this.state;

        const isInvalid =
            password === '' ||
            email === '';

        return (
            <form onSubmit={this.onSubmit}>
                <input
                    value={email}
                    onChange={event => this.setState(byPropKey('email', event.target.value))}
                    type="text"
                    placeholder="Email Address"
                />
                <input
                    value={password}
                    onChange={event => this.setState(byPropKey('password', event.target.value))}
                    type="password"
                    placeholder="Password"
                />
                <button disabled={isInvalid} type="submit">
                    Sign In
        </button>

                {error && <p>{error.message}</p>}
            </form>
        );
    }
}

//export default withRouter(SignInPage);
export default SignInForm;
export {
    SignInForm,
};

