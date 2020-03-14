
import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
    this.displayImage = this.displayImage.bind(this);
  }

  displayImage(ev){
    ev.preventDefault();
    if (ev.target.files && ev.target.files[0]) {
      this.setState({
        imageURL: URL.createObjectURL(ev.target.files[0])
      });
    }
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('imageFile', this.uploadInput.files[0]);

    fetch('http://192.168.225.25:3001/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        //alert(body.Data[29].result);
	document.getElementById('table').innerHTML = display_result(body);
      });
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage} >
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} onChange={this.displayImage} type="file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
        <br />
            <img id="target" src={this.state.imageURL} height="300vmin"  />
	    <br /><div id="table"></div>
     </form>
    );
  }

}

 function display_result(body){
        var s = '<table width="700vmin" border="1">';
	s += '<tr><td>SN</td><td>IMAGE</td><td>WIDTH</td><td>HEIGHT</td><td>ASPECT RATIO</td>';
	s += '<td>AREA</td><td>PERIMETER</td><td>RESULT</td></tr>';
	var result = '';
	for(var i=0; i < Object.keys(body.Data).length; i++){
		if(body.Data[i].result_ == 0){
			result = "Damage";
		}else{
			result = "No problem";
		}
		s += '<tr>';
		s += '<td>'+(i+1)+'</td><td>';
		//s += body.Data[i].image;
		s += '<img src="http://192.168.225.25:3001/get_images/extracted_grains_rgb/'+body.Data[i].image+'" height="100vmin" />'
		s += '</td><td>'+body.Data[i].width_.toFixed(2)+'</td><td>'+body.Data[i].height_.toFixed(2)+'</td>';
		s += '<td>'+body.Data[i].aspect_ratio_.toFixed(2)+'</td><td>'+body.Data[i].area_+'</td><td>'+body.Data[i].perimeter_.toFixed(2)+'</td><td>'+result+'</td>';
		s += '</tr>';
	}
	s += '</table>'
	return s;
  }


export default Main;
