import React from 'react';
import './App.css';
import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import {useState} from 'react';


// ckEditor 커스텀 버전 적용하는 방법 배워오기!!!!!!!!!


function App(){
  // const [poem, setPoem] = useState({
  //   title: '',
  //   content: ''
  // })

  const getValue = e=> {
    const {name, value} = e.target;
    console.log(name, value);
  }
  return (
    <div className="App">
      <div>
      
      </div>
      <div className='form-wrapper'>
        <input className="title-input" type='text' placeholder='제목' onChange={getValue} name='title'/>
        <CKEditor
          editor={ClassicEditor}
          config={{
            placeholder: "당신의 시를 쓰세요"
          }}
          onReady={editor => {
            console.log('Editor is ready to use!', editor);
          }}
          onChange={(event, editor) => {
            const data = editor.getData();
            console.log({ event, editor, data });
          }}
          onBlur={(event, editor) => {
            console.log('Blur.', editor);
          }}
          onFocus={(event, editor) => {
            console.log('Focus.', editor);
          }}
        />
        {/* <textarea className="text-area" placeholder='내용'></textarea> */}
      </div>
      <button className="submit-button" >시 완성!</button>
      <button className="submit-button">문장 도움 받기</button>
    </div>
    
  );
}







export default App;
