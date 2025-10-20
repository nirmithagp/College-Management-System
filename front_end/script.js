// Empty array: no colleges initially
const BASE_URL = "http://127.0.0.1:8000";

const colleges = [  
  {
    "id": "ed8d53d8-f61e-4623-bdc0-eed79b179dd6",
    "name": "BMS College of Engineering",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1946,
    "website": "https://bmsce.ac.in",
    "description": "One of the oldest engineering colleges in Karnataka with strong alumni network and industry connections."
  },
  {
    "id": "43b48f6c-a713-47a0-8547-95d33cd7557f",
    "name": "Bangalore Medical College and Research Institute",
    "location": "Bangalore, Karnataka, India",
    "type": "public",
    "established": 1955,
    "website": "https://bmcri.edu.in",
    "description": "Premier government medical college offering MBBS, MD/MS, and various medical programs."
  },
  {
    "id": "e9ee1c3d-e5cc-4a01-bea3-e87906b54a97",
    "name": "Bangalore University",
    "location": "Bangalore, Karnataka, India",
    "type": "public",
    "established": 1964,
    "website": "https://bangaloreuniversity.ac.in",
    "description": "Major state university offering undergraduate and postgraduate programs across multiple disciplines."
  },
  {
    "id": "f747356c-3641-4ac9-9ade-9d46c2a4caef",
    "name": "CMR Institute of Technology",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 2000,
    "website": "https://cmrit.ac.in",
    "description": "Growing engineering institute with emphasis on practical learning and industry exposure."
  },
  {
    "id": "cfa4572e-6382-45e3-95f3-7be58c015b26",
    "name": "Cambridge Institute of Technology",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1999,
    "website": "https://cambridge.edu.in",
    "description": "Private engineering college offering various engineering disciplines with modern facilities."
  },
  {
    "id": "31b2e131-c380-4001-a19c-c41d31f4e4e8",
    "name": "Christ University",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1969,
    "website": "https://christuniversity.in",
    "description": "Prestigious private university offering diverse programs in arts, science, commerce, engineering, and management."
  },
  {
    "id": "76c4dd12-8133-4ace-be78-c8a42c085b0c",
    "name": "Dayananda Sagar College of Engineering",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1979,
    "website": "https://dayanandasagar.edu",
    "description": "Popular private engineering college with modern infrastructure and diverse engineering programs."
  },
  {
    "id": "2a294fc1-0c7a-4000-a295-bbcfe1eeabdb",
    "name": "IIIT Bangalore",
    "location": "Bangalore, Karnataka, India",
    "type": "public",
    "established": 1999,
    "website": "https://iiitb.ac.in",
    "description": "Public-private partnership institute specializing in Information Technology, Computer Science, and Electronics & Communication."
  },
  {
    "id": "3aedfb96-26e6-44a0-8f97-d1f2cad16f65",
    "name": "Indian Institute of Science",
    "location": "Bangalore, Karnataka, India",
    "type": "public",
    "established": 1909,
    "website": "https://iisc.ac.in",
    "description": "India's premier institute for advanced scientific and technological research and education, ranked #1 in research."
  },
  {
    "id": "77550907-1709-49e9-849e-3afca1d381b2",
    "name": "Jain University",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1990,
    "website": "https://jainuniversity.ac.in",
    "description": "Multi-disciplinary private university offering programs across engineering, management, arts, and sciences."
  },
  {
    "id": "96da1d28-416b-4333-850a-170afc8581e4",
    "name": "Kempegowda Institute of Medical Sciences",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1980,
    "website": "https://kims-bangalore.edu.in",
    "description": "Well-established private medical college offering comprehensive medical education."
  },
  {
    "id": "c663aa7b-4ce7-4ce3-bb9e-7d5c265a5a7f",
    "name": "M.S. Ramaiah Institute of Technology",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1962,
    "website": "https://msrit.edu",
    "description": "Premier private engineering institute known for its academic excellence and industry partnerships."
  },
  {
    "id": "7a5ff138-4755-404b-851a-0b0945ae5875",
    "name": "M.S. Ramaiah Medical College",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1979,
    "website": "https://msrmc.ac.in",
    "description": "Leading private medical college with state-of-the-art facilities and research programs."
  },
  {
    "id": "219a1a5d-abeb-4f12-b212-ff6d8897129e",
    "name": "Mount Carmel College",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1948,
    "website": "https://mccblr.edu.in",
    "description": "Premier women's college offering undergraduate and postgraduate programs in various disciplines."
  },
  {
    "id": "ad732303-7329-4ab1-a723-a7729b8afd81",
    "name": "New Horizon College of Engineering",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 2001,
    "website": "https://newhorizonindia.edu",
    "description": "Modern engineering college offering industry-relevant programs with focus on innovation and research."
  },
  {
    "id": "a0e6149d-e3a9-4002-adef-edd87c56cb7d",
    "name": "PES University",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1972,
    "website": "https://pes.edu",
    "description": "Leading private university offering engineering, management, medicine, and other professional programs."
  },
  {
    "id": "99cf3a0b-3f5f-4b2a-8b12-0d320589cd9a",
    "name": "R.V. College of Engineering",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1963,
    "website": "https://rvce.edu.in",
    "description": "One of the top private engineering colleges in Karnataka offering all engineering streams with excellent placements."
  },
  {
    "id": "8920b0ad-8b98-400d-bd63-7f18889fc75e",
    "name": "Sir M. Visvesvaraya Institute of Technology",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1986,
    "website": "https://sirmvit.edu",
    "description": "Well-established private engineering college offering undergraduate and postgraduate programs."
  },
  {
    "id": "e84f5528-0967-408e-ab45-be54898ca33c",
    "name": "St. John's Medical College",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1963,
    "website": "https://stjohns.in",
    "description": "Prestigious private medical college known for its clinical excellence and research facilities."
  },
  {
    "id": "630bf4b7-07f5-4d86-8f0f-5b43ffb1115b",
    "name": "St. Joseph's College",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1882,
    "website": "https://sjc.ac.in",
    "description": "Historic college known for excellence in arts, science, and commerce education."
  },
  {
    "id": "08307307-0943-4dfa-869d-2e249e0fcb83",
    "name": "St. Joseph's College of Commerce",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1972,
    "website": "https://sjcc.edu.in",
    "description": "Leading commerce college known for its business and management programs."
  },
  {
    "id": "f6c368f9-09fd-49af-a5ca-8c08610db065",
    "name": "University Visvesvaraya College of Engineering",
    "location": "Bangalore, Karnataka, India",
    "type": "public",
    "established": 1917,
    "website": "https://uvce.ac.in",
    "description": "Premier government engineering college affiliated to Bangalore University, known for its legacy and excellence."
  },
  {
    "id": "6a7c52d2-6d47-4bb7-97b5-7dcb4f8482fe",
    "name": "Vydehi Institute of Medical Sciences",
    "location": "Bangalore, Karnataka, India",
    "type": "private",
    "established": 1999,
    "website": "https://vydehi.ac.in",
    "description": "Modern private medical college with advanced medical facilities and research centers."
  }
];

// Fake login
function login() {
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;

  // Accept any input — no validation
  if (user && pass) {
    document.getElementById("loginPage").style.display = "none";
    document.getElementById("mainApp").style.display = "block";
    renderColleges(colleges); // renders nothing at first
  } else {
    alert("Please enter username and password");
  }
}

function renderColleges(list) {
  const container = document.getElementById("collegeList");
  container.innerHTML = "";

  if (list.length === 0) {
    container.innerHTML = "<p>No colleges found. Please add one.</p>";
    return;
  }

  list.forEach(college => {
    const card = document.createElement("div");
    card.className = "college-card";
    card.innerHTML = `
      <strong>${college.name}</strong><br/>
      <small>${college.location} | ${college.year} | <em>${college.type}</em></small><br/>
      <a href="${college.website}" target="_blank">${college.website}</a><br/>
      <p>${college.description}</p>
    `;
    container.appendChild(card);
  });
}

function showAddForm() {
  document.getElementById("collegeModal").style.display = "flex";
}

function closeModal() {
  document.getElementById("collegeModal").style.display = "none";
  document.getElementById("collegeForm").reset();
}

// Add new college
document.getElementById("collegeForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const newCollege = {
    name: document.getElementById("collegeName").value,
    location: document.getElementById("location").value,
    year: document.getElementById("year").value,
    type: document.getElementById("collegeType").value,
    website: document.getElementById("website").value,
    description: document.getElementById("description").value
  };

  colleges.push(newCollege);
  renderColleges(colleges);
  closeModal();
});

// Filtering
function filterColleges() {
  const search = document.getElementById("searchInput").value.toLowerCase();
  const type = document.getElementById("typeFilter").value;
  const location = document.getElementById("locationFilter").value;

  const filtered = colleges.filter(college => {
    return (
      (college.name.toLowerCase().includes(search) || college.location.toLowerCase().includes(search)) &&
      (type === "all" || college.type === type) &&
      (location === "all" || college.location.toLowerCase().includes(location.toLowerCase()))
    );
  });

  renderColleges(filtered);
}

// Attach filter handlers
document.getElementById("searchInput").addEventListener("input", filterColleges);
document.getElementById("typeFilter").addEventListener("change", filterColleges);
document.getElementById("locationFilter").addEventListener("change", filterColleges);
