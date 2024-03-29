import logo from './logo.svg';
import React from 'react'
import './App.css';

class App extends React.Component {

  constructor(props){
    super(props)
      this.state = {
        todoList: [],
        activeItem:{
          id: null,
          title: "",
          complete: false
        },
        editing: false
      }
      this.fetchTasks = this.fetchTasks.bind(this)
      this.handleChange = this.handleChange.bind(this)
      this.handleSubmit = this.handleSubmit.bind(this)
      this.getCookie = this.getCookie.bind(this)

      this.deleteItem = this.deleteItem.bind(this)
      this.startEdit = this.startEdit.bind(this)
      this.strikeUnstrike = this.strikeUnstrike.bind(this)
  }
  getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

  componentWillMount(){
    this.fetchTasks()
  }

  fetchTasks(){
    console.log("Fetching")
    fetch("http://localhost:8000/api/task-list/")
      .then(response => response.json())
      .then(data => {
        this.setState({
          todoList: data
        })
      })
  }

  handleChange(e){
    var name = e.target.name
    var value = e.target.value
    this.setState({
      activeItem:{
        ...this.state.activeItem,
        title: value
      }
    })
  }

  handleSubmit(e){
    e.preventDefault()
    console.log('ITEM', this.state.activeItem)
    var csrftoken = this.getCookie('csrftoken')

    var url = 'http://localhost:8000/api/task-create/'
    if(this.state.editing){
      var url = `http://localhost:8000/api/task-update/${this.state.activeItem.id}/`
      this.setState({
        editing: false
      })
    }
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify(this.state.activeItem)
    })
      .then(response=>{
        this.fetchTasks()
        this.setState({
          id: null,
          title: '',
          complete: false
        })
      })
        .catch(e=> console.log(e))
  }


  startEdit(task){
    this.setState({
      activeItem:task,
      editing:true
    })
  }


  deleteItem(task){
    var csrftoken = this.getCookie('csrftoken')

    fetch(`http://localhost:8000/api/task-delete/${task.id}/`, {
      method: 'DELETE',
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken
      }
    })
      .then((responde)=>{
        this.fetchTasks()
      })
  }


  strikeUnstrike(task){
    task.completed = !task.completed
    var csrftoken = this.getCookie('csrftoken')
    var url = `http://localhost:8000/api/task-update/${task.id}/`

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body : JSON.stringify({'completed': task.completed, 'title': task.title})
    }).then((response) => {
        this.fetchTasks()
      })
  }
  render(){
    var tasks = this.state.todoList
    var self = this
    return(
      <div className='container'>
        <div id='task-container'>
          <div id='form-container'>
              <form id="form" onSubmit={this.handleSubmit}>
                <div className="flex-wrapper">
                  <div style={{flex: 6}}>
                    <input className="form-control" id="title" type="text" name="title" value={this.state.activeItem.title} placeholder="Adicionar tarefa..." onChange={this.handleChange} />
                  </div>

                  <div style={{flex: 1}}>
                    <input id="submit" className="btn btn-warning" type="submit" name="Add" />
                  </div>
                </div>
              </form>
          </div>
          <div className='list-wrapper'>{tasks.map((task, index)=>{
            return(
              <div key={index} className='task-wrapper flex-wrapper'>
                <div onClick={()=> self.strikeUnstrike(task)} style={{flex: 7}}>
                  {task.completed==false ? (
                    <span>{task.title}</span>
                  ) : (
                    <strike>{task.title}</strike>
                  )}
                  
                </div>
                <div style={{flex: 1}}>
                  <button onClick={()=>self.startEdit(task)} className='btn btn-sm btn-outline-info'>Editar</button>
                </div>
                <div style={{flex: 1}}>
                  <button onClick={()=>self.deleteItem(task)} className='btn btn-sm btn-outline-dark delete'>-</button>
                </div>
              </div>
            )
          })}</div>
        </div>
      </div>
    )
  }
}

export default App;
