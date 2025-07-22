import React, { useEffect, useState } from 'react';
import axios from 'axios';

function JobList() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/jobs/')
      .then((res) => {
        setJobs(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setError('Failed to fetch jobs');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading jobs...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div>
      <h2>Available Jobs</h2>
      <ul>
        {jobs.map((job) => (
          <li key={job.id}>
            <strong>{job.title}</strong> at {job.company} ({job.location})
            <p>{job.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default JobList;
