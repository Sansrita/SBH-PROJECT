import logo from './logo.svg';
import './App.css';

function App() {
  return (
   <>
   <ul class="nav nav-pills">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Header</a>
  </li>
  </ul>
   <form>
  <div className="form-group row">
    <label for="name" className="col-sm-2 col-form-label"></label>
    <div className="col-sm-10">
      <input type="name" className="form-control" id="name" placeholder=" Please enter your Name"/>
    </div>
  </div>
  <div className="form-group row">
    <label for="age" className="col-sm-2 col-form-label"></label>
    <div className="col-sm-10">
      <input type="age" className="form-control" id="age" placeholder="Please Enter Your age"/>
    </div>
  </div>
  <div className="form-group row">
    <label for="address" className="col-sm-2 col-form-label"></label>
    <div className="col-sm-10">
      <input type="name" className="form-control" id="name" placeholder=" Please enter your Address"/>
    </div>
  </div>
  <div className="form-group row">
    <label for="number" className="col-sm-2 col-form-label"></label>
    <div className="col-sm-10">
      <input type="name" className="form-control" id="name" placeholder=" Please enter your Phone Number"/>
    </div>
  </div>
  <div className="form-group">
    <div className="row">
      <legend className="col-form-label col-sm-2 pt-0">Gender</legend>
      <div className="col-sm-10">
        <div className="form-check">
          <input className="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1"/>
          <label className="form-check-label" for="gridRadios1">
            Male
          </label>
        </div>
        <div className="form-check">
          <input className="form-check-input" type="radio" name="gridRadios" id="gridRadios2" value="option2"/>
          <label className="form-check-label" for="gridRadios2">
            Female
          </label>
        </div>
        <div className="form-check disabled">
          <input className="form-check-input" type="radio" name="gridRadios" id="gridRadios3" value="option3" />
          <label className="form-check-label" for="gridRadios3">
            Transgender 
          </label>
        </div>
      </div>
    </div>
  </div>
  <label class="my-1 mr-2" for="inlineFormCustomSelectPref">Your Weight:     </label>
  <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref">
    <option selected>Choose...</option>
    <option value="1">10-20</option>
    <option value="2">21-30</option>
    <option value="3">31-40</option>
    <option value="3">41-50</option>
    <option value="3">51-60</option>
    <option value="3">61-70</option>
    <option value="3">71-80</option>
    <option value="3">81-90</option>
    <option value="3">91-100</option>
    <option value="3">101-110</option>
    <option value="3">111-120</option>
    <option value="3">121-130</option>
    <option value="3">More than 130</option>
  </select>
  <div className="form-group row">
    <div className="col-sm-2"></div>
    <div className="col-sm-10">
      <div className="form-check">
        <input className="form-check-input" type="checkbox" id="gridCheck1"/>
        <label className="form-check-label" for="gridCheck1">
          Remember Me
        </label>
      </div>
    </div>
  </div>
  <div className="form-group row">
    <div className="col-sm-10">
      <button type="submit" className="btn btn-primary">Sign in</button>
    </div>
  </div>
</form>
    </>
    
    
  );
}

export default App;
