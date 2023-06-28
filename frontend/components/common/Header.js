'use client';
import React, { useEffect, useState } from 'react';
import { Button, Dropdown, Navbar, Avatar } from 'flowbite-react';

async function getCategorys() {
  const response = await fetch("http://127.0.0.1:8000/categorys/", { cache: "no-store" });
  const data = await response.json();
  return data;
}

export default async function Header({ params, searchParams }) {
  const [categorys, setCategorys] = useState([]);
  // const categorys = await getCategorys();
  useEffect(() => {
    async function fetchData() {
      const data = await getCategorys();
      setCategorys(data);
    }

    fetchData();
  }, []);
  console.log(categorys)
  return (
    <Navbar
      fluid
      // rounded
      className='bg-blue-500'
    >
      <Navbar.Brand href="/">
        <img
          alt="Flowbite React Logo"
          className="mr-3 h-6 sm:h-9"
          src="/lion.jpg"
        />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
          MyBlog
        </span>
      </Navbar.Brand>
      <div className="flex md:order-2">
        <Dropdown
          inline
          label={<Avatar alt="User settings" img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" rounded/>}
        >
          <Dropdown.Header>
            <span className="block text-sm">
              Bonnie Green
            </span>
            <span className="block truncate text-sm font-medium">
              name@flowbite.com
            </span>
          </Dropdown.Header>
          <Dropdown.Item>
            Dashboard
          </Dropdown.Item>
          <Dropdown.Item>
            Settings
          </Dropdown.Item>
          <Dropdown.Item>
            Earnings
          </Dropdown.Item>
          <Dropdown.Divider />
          <Dropdown.Item>
            Sign out
          </Dropdown.Item>
        </Dropdown>
        <Navbar.Toggle />
      </div>
      <Navbar.Collapse>
        <Navbar.Link
          active
          href="#"
        >
          <p>
            Home
          </p>
        </Navbar.Link>
        <Navbar.Link href="#">
          About
        </Navbar.Link>
        <Navbar.Link href="#">
          Services
        </Navbar.Link>
        <Navbar.Link href="#">
          Pricing
        </Navbar.Link>
        <Navbar.Link href="#">
          Contact
        </Navbar.Link>
        <Dropdown
          inline
          label="Categories"
        >
          {categorys?.map((category) => (
            <Dropdown.Item>
              Dashboard
          </Dropdown.Item>
          ))}
          <Dropdown.Item>
            Dashboard
          </Dropdown.Item>
          <Dropdown.Item>
            Settings
          </Dropdown.Item>
          <Dropdown.Item>
            Earnings
          </Dropdown.Item>
          <Dropdown.Item>
            Sign out
          </Dropdown.Item>
        </Dropdown>
      </Navbar.Collapse>
    </Navbar>
  );
}

// export async function getStaticProps() {
//   const response = await fetch('http://127.0.0.1:8000/posts/')
//   const categorys = await response.json();

//   return {
//     props: {
//       categorys,
//     }
//   }
// }