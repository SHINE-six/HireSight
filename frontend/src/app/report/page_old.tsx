'use client';

import React, { useState, useEffect, useRef } from 'react';
import { usePdf } from 'react-pdf-js';
 
const MyPdfViewer = () => {
  const [page, setPage] = useState(1);
  const [pages, setPages] = useState(null);
 
  const renderPagination = (page: number, pages: null) => {
    if (!pages) {
      return null;
    }
    let previousButton = <li className="previous" onClick={() => setPage(page - 1)}><a href="#"><i className="fa fa-arrow-left"></i> Previous</a></li>;
    if (page === 1) {
      previousButton = <li className="previous disabled"><a href="#"><i className="fa fa-arrow-left"></i> Previous</a></li>;
    }
    let nextButton = <li className="next" onClick={() => setPage(page + 1)}><a href="#">Next <i className="fa fa-arrow-right"></i></a></li>;
    if (page === pages) {
      nextButton = <li className="next disabled"><a href="#">Next <i className="fa fa-arrow-right"></i></a></li>;
    }
    return (
      <nav>
        <ul className="pager">
          {previousButton}
          {nextButton}
        </ul>
      </nav>
    );
  }
 
  const canvasEl = useRef<HTMLCanvasElement | null>(null);
 
  const [loading, numPages] = usePdf({
    file: 'report/Interview Conversation Log Report - Good One.pdf',
    page,
    canvasEl: canvasEl,
  });
 
  useEffect(() => {
    setPages(numPages);
  }, [numPages]);
 
  return (
    <div className='bg-red-300 flex justify-center'>
      {loading && <span>Loading...</span>}
      <canvas ref={canvasEl} />
      {renderPagination(page, pages)}
    </div>
  );
}
 
export default MyPdfViewer;